# train.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

print("✅ Loading dataset...")

# Load dataset
df = pd.read_csv("spam.csv", usecols=[0, 1], names=['label', 'text'], header=0)

# Map labels to numeric
y = df['label'].map({'ham': 0, 'spam': 1})
X_text = df['text']

# Convert text to numeric features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X_text)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"✅ Model trained. Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# Save model and vectorizer
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("📁 Saved spam_model.pkl and vectorizer.pkl")
