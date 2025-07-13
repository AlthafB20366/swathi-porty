from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Projects Page
@app.route("/projects")
def projects():
    return render_template("projects.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Resume Download Route
@app.route("/resume")
def resume():
    return send_from_directory("resume", "swathi_resume.pdf")

if __name__ == "__main__":
    app.run(debug=True)
