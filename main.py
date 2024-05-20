from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap5
from datetime import datetime
year = datetime.now().year

app = Flask(__name__)
Bootstrap5(app)


@app.route('/')
def home():
    return render_template('index.html', year=year)


@app.route('/resume')
def resume():
    return render_template('resume.html', year=year)


@app.route('/download-resume')
def down_resume():
    return send_from_directory(directory='', path='Khushi Khare Resume.pdf')


@app.route('/projects')
def projects():
    return render_template('projects.html', year=year)


@app.route('/contact')
def contact():
    return render_template('contact.html', year=year)


@app.route("/da-projects")
def da_projects():
    return render_template('da.html', year=year)


@app.route('/python-projects')
def py_projects():
    return render_template('py_projects.html', year=year)


# if __name__ == "__main__":
#     app.run(debug=True)

