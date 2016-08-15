from wtforms import Form, SelectField, BooleanField, validators

class ScoreForm(Form):
	playerScores = {}

	selfDraw = BooleanField('Drew Last Tile', [validators.DataRequired()])
	winner = SelectField('Winner')

	def AddPlayers(self, players):
		playerNames = []
		for player in players:
			self.playerScores[player] = 0
			playerNames.append((player, player))
		self.winner.choices = playerNames




