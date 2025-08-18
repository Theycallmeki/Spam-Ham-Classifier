# Spam Detection Web App

A simple **Flask web application** that classifies emails as **spam** or **ham (not spam)** using a machine learning model trained on a `spam.csv` dataset. Users can add emails, see predictions, and manage the database through the web interface.

---

## Table of Contents

1. [Requirements](#1-requirements)  
2. [Setup Instructions](#2-setup-instructions)  
3. [Database Initialization](#3-database-initialization)  
4. [Training the Model](#4-training-the-model)  
5. [Running the Application](#5-running-the-application)  
6. [Using the App](#6-using-the-app)  
7. [File Structure](#7-file-structure)  
8. [Getting Started (Quick Setup)](#8-getting-started-quick-setup)  

---

## 1. Requirements

Key packages:

- Flask
- pandas
- scikit-learn
- joblib
- numpy

---

## 2. Setup Instructions

Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3. Database Initialization
The app uses SQLite to store email records.

Database file: emails.db

The database is automatically created when running the app for the first time.

Table structure:

Column	Type
id	INTEGER PRIMARY KEY AUTOINCREMENT
content	TEXT
true_label	TEXT
prediction	TEXT

4. Training the Model
Ensure your CSV file has columns: text and label

text → email content

label → "spam" or "ham"

Run the training script:

bash
Copy
Edit
python train.py
This will:

Split the dataset into training and testing sets

Vectorize text using CountVectorizer

Train a Multinomial Naive Bayes model

Save spam_model.pkl and vectorizer.pkl for the Flask app

After training, the script prints the model accuracy.

5. Running the Application
Start the Flask server:

bash
Copy
Edit
python app.py
Access the web app at http://127.0.0.1:5000

Add new emails through the form and see predictions

Delete emails using the "Delete" button

6. Using the App
Add email: Enter email content and optionally provide the true label

View emails: All emails are displayed in a table with predictions

Delete emails: Remove entries from the database

7. File Structure
bash
Copy
Edit
spam-detection-app/
├── app.py               # Flask app
├── train.py             # Model training script
├── spam_model.pkl       # Saved ML model (after training)
├── vectorizer.pkl       # Saved CountVectorizer (after training)
├── spam.csv             # Dataset for training
├── emails.db            # SQLite database (auto-created)
├── templates/
│   └── index.html       # Web interface
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
8. Getting Started (Quick Setup)
Clone and navigate to the repository:

bash
Copy
Edit
git clone <your-repo-url>
cd <your-repo-folder>
Create virtual environment and activate:

bash
Copy
Edit
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Train the model:

bash
Copy
Edit
python train.py
Run the web app:

bash
Copy
Edit
python app.py
Open your browser at http://127.0.0.1:5000 to start adding emails and testing spam predictions.
