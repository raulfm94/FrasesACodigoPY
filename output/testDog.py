class Dog:
	mood = "HAPPY"
	energy = 100
	coordenatePosition = (0,0)

	def Run(self):
		self.MoveForward(2)
		self.energy -= 1
		self.mood = "PLAY"
		return 0

	def MoveForward(self, numbersSteps):
		self.coordenatePosition[0] += numbersSteps
		self.mood = "MOVING"
		self.energy -= 1

	def MoveLeft(self, numbersSteps):
		self.coordenatePosition[1] -= numbersSteps
		self.mood = "MOVING"
		self.energy -= 1

	def MoveRight(self, numbersSteps):
		self.coordenatePosition[1] += numbersSteps
		self.mood = "MOVING"
		self.energy -= 1

	def Bark(self):
		print "barf, bark"
		self.energy -= 1
		self.mood = "BARKING"

	def Lay(self):
		print "relax"
		print "move the Booty"
		self.energy += 3

	def Check(self):
		print "mood: " + self.mood
		print "energy: " + str(self.energy)
		print "Position: " + str(self.coordenatePosition) 