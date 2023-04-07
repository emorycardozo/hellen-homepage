from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/contato')
def contact():
    return render_template('contact.html')


@app.route('/projetos')
def projects():
    return render_template('projects.html')


@app.route('/quemsou')
def resume():
    return render_template('resume.html')
