from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


# @app.route('/contato')
# def contact():
#     return render_template('contact.html')

@app.route('/artigos')
def artigos():
    return render_template('artigos.html')


@app.route('/projetos')
def projects():
    return render_template('projects.html')


@app.route('/quemsou')
def resume():
    return render_template('resume.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')
