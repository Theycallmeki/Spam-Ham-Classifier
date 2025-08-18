<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Spam Detection Web App</title>
</head>
<body>

<h1>Spam Detection Web App</h1>

<p>A simple <strong>Flask web application</strong> that classifies emails as <strong>spam</strong> or <strong>ham (not spam)</strong> using a machine learning model trained on a <code>spam.csv</code> dataset. Users can add emails, see predictions, and manage the database through the web interface.</p>

<hr>

<h2>Table of Contents</h2>
<ol>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#setup-instructions">Setup Instructions</a></li>
    <li><a href="#database-initialization">Database Initialization</a></li>
    <li><a href="#training-the-model">Training the Model</a></li>
    <li><a href="#running-the-application">Running the Application</a></li>
    <li><a href="#using-the-app">Using the App</a></li>
    <li><a href="#file-structure">File Structure</a></li>
    <li><a href="#getting-started-quick-setup">Getting Started (Quick Setup)</a></li>
</ol>

<h2 id="requirements">1. Requirements</h2>
<p>Key packages:</p>
<ul>
    <li>Flask</li>
    <li>pandas</li>
    <li>scikit-learn</li>
    <li>joblib</li>
    <li>numpy</li>
</ul>

<h2 id="setup-instructions">2. Setup Instructions</h2>
<p>Clone the repository:</p>
<pre><code>git clone &lt;your-repo-url&gt;
cd &lt;your-repo-folder&gt;</code></pre>

<p>Create a virtual environment (recommended):</p>
<pre><code>python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate</code></pre>

<p>Install dependencies:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2 id="database-initialization">3. Database Initialization</h2>
<p>The app uses SQLite to store email records.</p>
<p>Database file: <code>emails.db</code></p>
<p>The database is automatically created when running the app for the first time.</p>
<p>Table structure:</p>
<table border="1" cellspacing="0" cellpadding="5">
    <tr>
        <th>Column</th>
        <th>Type</th>
    </tr>
    <tr>
        <td>id</td>
        <td>INTEGER PRIMARY KEY AUTOINCREMENT</td>
    </tr>
    <tr>
        <td>content</td>
        <td>TEXT</td>
    </tr>
    <tr>
        <td>true_label</td>
        <td>TEXT</td>
    </tr>
    <tr>
        <td>prediction</td>
        <td>TEXT</td>
    </tr>
</table>

<h2 id="training-the-model">4. Training the Model</h2>
<p>Ensure your CSV file has columns: <code>text</code> and <code>label</code></p>
<ul>
    <li><code>text</code> → email content</li>
    <li><code>label</code> → "spam" or "ham"</li>
</ul>

<p>Run the training script:</p>
<pre><code>python train.py</code></pre>

<p>This will:</p>
<ul>
    <li>Split the dataset into training and testing sets</li>
    <li>Vectorize text using CountVectorizer</li>
    <li>Train a Multinomial Naive Bayes model</li>
    <li>Save <code>spam_model.pkl</code> and <code>vectorizer.pkl</code> for the Flask app</li>
</ul>
<p>After training, the script prints the model accuracy.</p>

<h2 id="running-the-application">5. Running the Application</h2>
<p>Start the Flask server:</p>
<pre><code>python app.py</code></pre>

<p>Access the web app at <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a></p>
<ul>
    <li>Add new emails through the form and see predictions</li>
    <li>Delete emails using the "Delete" button</li>
</ul>

<h2 id="using-the-app">6. Using the App</h2>
<ul>
    <li><strong>Add email:</strong> Enter email content and optionally provide the true label</li>
    <li><strong>View emails:</strong> All emails are displayed in a table with predictions</li>
    <li><strong>Delete emails:</strong> Remove entries from the database</li>
</ul>

<h2 id="file-structure">7. File Structure</h2>
<pre><code>spam-detection-app/
│
├── app.py               # Flask app
├── train.py             # Model training script
├── spam_model.pkl       # Saved ML model (after training)
├── vectorizer.pkl       # Saved CountVectorizer (after training)
├── spam.csv             # Dataset for training
├── emails.db            # SQLite database (auto-created)
├── templates/
│   └── index.html       # Web interface
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation</code></pre>

<h2 id="getting-started-quick-setup">8. Getting Started (Quick Setup)</h2>
<pre><code>git clone &lt;your-repo-url&gt;
cd &lt;your-repo-folder&gt;
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
python train.py           # Train the model
python app.py             # Run the web app</code></pre>

<p>Then open your browser at <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a></p>
<p>You can immediately start adding emails and testing spam predictions.</p>

</body>
</html>
