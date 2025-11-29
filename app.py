from flask import Flask, render_template, abort
from flask_frozen import Freezer
from publications import publications

app = Flask(__name__)

@app.route('/')
def render_index():
    return render_template("index.html")

@app.route('/about.html')
def render_about():
    return render_template("about.html")

@app.route('/publications.html')
def render_publications():
    return render_template("publications.html", publications=publications)

@app.route('/publications/<pub_id>/')
def render_publication(pub_id):
    pub = next((p for p in publications if p["id"] == pub_id), None)
    if pub is None:
        abort(404)
    return render_template("publication_single.html", pub=pub)

freezer = Freezer(app)

@freezer.register_generator
def publication_routes():
    for pub in publications:
        yield 'render_publication', {'pub_id': pub["id"]}

if __name__ == '__main__':
    freezer.freeze()
    app.run()