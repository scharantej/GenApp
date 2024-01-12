 
# Import necessary libraries
from flask import Flask, render_template, request
import os

# Create a Flask app
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    """Renders the index page."""
    return render_template('index.html')

@app.route('/tutorials')
def tutorials():
    """Renders the tutorials page."""
    return render_template('tutorials.html')

@app.route('/tutorials/<tutorial_id>')
def tutorial_detail(tutorial_id):
    """Renders the tutorial detail page."""
    return render_template('tutorial-detail.html', tutorial_id=tutorial_id)

@app.route('/articles')
def articles():
    """Renders the articles page."""
    return render_template('articles.html')

@app.route('/articles/<article_id>')
def article_detail(article_id):
    """Renders the article detail page."""
    return render_template('article-detail.html', article_id=article_id)

@app.route('/code-samples')
def code_samples():
    """Renders the code samples page."""
    return render_template('code-samples.html')

@app.route('/code-samples/<code_sample_id>')
def code_sample_detail(code_sample_id):
    """Renders the code sample detail page."""
    return render_template('code-sample-detail.html', code_sample_id=code_sample_id)

@app.route('/playground')
def playground():
    """Renders the playground page."""
    return render_template('playground.html')

@app.route('/forum')
def forum():
    """Renders the forum page."""
    return render_template('forum.html')

@app.route('/forum/<discussion_id>')
def discussion_detail(discussion_id):
    """Renders the discussion detail page."""
    return render_template('discussion-detail.html', discussion_id=discussion_id)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
