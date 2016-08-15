from wtforms import Form, StringField, validators

class SetupForm(Form):
	player1 = StringField('Player1', [validators.Length(min=1, max=25)])
	player2 = StringField('Player2', [validators.Length(min=1, max=25)])
	player3 = StringField('Player3', [validators.Length(min=1, max=25)])
	player4 = StringField('Player4', [validators.Length(min=1, max=25)])
