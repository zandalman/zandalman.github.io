from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)

@app.route('/')
def render_index():
    return render_template("index.html")

@app.route('/about.html')
def render_about():
    return render_template("about.html")

@app.route('/research.html')
def render_research():
    return render_template("research.html")

freezer = Freezer(app)

if __name__ == '__main__':
        freezer.freeze()
        app.run()