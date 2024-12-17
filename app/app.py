from flask import Flask, render_template

app = Flask(__name__)

# List of blog posts
blog_posts = [
    {
        "title": "My First Blog Post",
        "date": "January 1, 2024",
        "content": "This is my first blog post! I'm excited to start sharing my journey.",
        "link": "#"
    },
    {
        "title": "Exploring Flask",
        "date": "February 5, 2024",
        "content": "Flask is an amazing microframework for building web applications.",
        "link": "#"
    },
    {
        "title": "Learning Python",
        "date": "March 15, 2024",
        "content": "Python is versatile and fun to learn. Here's how I started my Python journey.",
        "link": "#"
    }
]

@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
