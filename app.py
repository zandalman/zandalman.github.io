from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_index():
    return render_template("index.html")

@app.route('/about')
def render_about():
    return render_template("about.html")

@app.route('/research')
def render_research():
    return render_template("research.html")

if __name__ == '__main__':
    app.run()
