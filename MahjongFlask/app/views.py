from flask import render_template, request, redirect, url_for
from app import app
from forms.setup_form import SetupForm
from forms.score_form import ScoreForm

players = []

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='MahJong Tracker')

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    form = SetupForm(request.form)
    if request.method == 'POST' and form.validate():
        if len(players) <= 0:
            players.append(request.form.get("player1"))
            players.append(request.form.get("player2"))
            players.append(request.form.get("player3"))
            players.append(request.form.get("player4"))
        form = ScoreForm(request.form)
        return redirect(url_for('game'))
    #print players
    return render_template('setup.html', form=form)


@app.route('/game', methods=['GET', 'PUT'])
def game():
    #print players
    form = ScoreForm(request.form)
    form.AddPlayers(players)
    print form.winner
    if request.method == 'PUT':
        print "PUT \n"
    return render_template('game.html', players=players, form=form)