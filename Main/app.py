from flask import Flask, request, render_template, redirect
import sqlite3
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# --- Load model and vectorizer ---
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# --- Calculate accuracy once at startup ---
df = pd.read_csv("spam.csv", usecols=[0, 1], names=['label', 'text'], header=0, encoding='latin-1')
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
X_full = vectorizer.transform(df['text'])
y_full = df['label_num']
accuracy = accuracy_score(y_full, model.predict(X_full))

# --- Flask app ---
app = Flask(__name__)

# --- SQLite DB ---
DB_FILE = "emails.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            prediction TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --- Routes ---
@app.route("/")
def home():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emails")
    emails = cursor.fetchall()
    conn.close()
    return render_template("index.html", emails=emails, accuracy=accuracy)

@app.route("/add", methods=["POST"])
def add_email():
    content = request.form["content"]

    try:
        features = vectorizer.transform([content])
        prediction = model.predict(features)[0]
        result = "Spam" if prediction == 1 else "Ham"
    except Exception as e:
        result = f"Error: {e}"

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emails (content, prediction) VALUES (?, ?)", (content, result))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:email_id>")
def delete_email(email_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM emails WHERE id=?", (email_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
