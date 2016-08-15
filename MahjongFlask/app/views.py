from flask import render_template, request
from app import app
from forms.setup_form import SetupForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='MahJong Tracker')

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    form = SetupForm(request.form)
    return render_template('setup.html', form=form)