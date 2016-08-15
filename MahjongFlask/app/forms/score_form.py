from wtforms import Form, StringField, BooleanField, validators

class ScoreForm(Form):
	playerScores = {}

	selfDraw = BooleanField('Drew Last Tile', [validators.DataRequired()])

	def AddPlayers(self, players):
		for player in players:
			self.playerScores[player] = 0




