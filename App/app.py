from flask import Flask, render_template, redirect, url_for, request, escape, g
from BalabobaBackend.balaboba import get_text, get_comments
from BalabobaBackend.helpers import connect_db, get_old_wikis
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('BalabobaBackend/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.route('/')
def index():
    return redirect(url_for('wiki_search'))


@app.route('/wiki/')
def wiki_search():
    if 'q' in request.args.keys():
        q = escape(request.args.get('q'))
        return redirect(url_for('wiki_show', q=q))
    return render_template('search.html')


@app.route('/wiki/<q>')
def wiki_show(q):
    if 'q' in request.args.keys():
        q = escape(request.args.get('q'))
        return redirect(url_for('wiki_show', q=q))
    texts = get_text(q)
    comments = get_comments(q)
    return render_template('wiki.html', q=q, texts=texts, comments=comments)


@app.route('/loading_texts')
def get_loading_texts():
    with open("data/waiting.json") as f:
        data = json.loads(f.read())
    print(data)
    return data


if __name__ == '__app__':
    init_db()
    app.run()