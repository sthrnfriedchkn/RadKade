class data_container:
	def __init__(self, title, description, genre, year, players, rating, visible):
		self.title = title
		self.description = description
		self.genre = genre
		self.year = year
		self.players = players
		self.rating = rating
		self.visible = visible
		
	def setVisible(self, value):
		self.visible = value
	
	def dumpData(self):
		print "Title: ", self.title, ", Description: ", self.description, ", Genre: ", self.genre, ", Year: ", self.year, ", Players: ", self.players, ", Rating: ", self.rating