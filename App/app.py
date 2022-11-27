from flask import Flask, render_template, redirect, url_for, request, escape
from BalabobaBackend.balaboba import get_text, get_comments
app = Flask(__name__)


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
    texts = get_text(q)
    comments = get_comments(q)
    return render_template('wiki.html', q=q, texts=texts, comments=comments)


if __name__ == '__app__':
    app.run()