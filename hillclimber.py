import copy
import numpy as np

from solution import SOLUTION
import constants as c


class HILL_CLIMBER:

	def __init__(self):

		self.parent = SOLUTION()
		self.fitnessOverTimeParent = np.zeros(c.NUMBER_OF_GENERATIONS)
		self.fitnessOverTimeChild = np.zeros(c.NUMBER_OF_GENERATIONS)

	def Evolve(self):
		self.parent.Evaluate(GUI=True)

		for currentGeneration in range(c.NUMBER_OF_GENERATIONS):

			self.Evolve_For_One_Generation()

			self.fitnessOverTimeChild[currentGeneration] = self.child.fitness
			self.fitnessOverTimeParent[currentGeneration] = self.parent.fitness


		self.SaveFitnessData()

		
	def ShowBest(self):
		self.parent.Evaluate(GUI=True)

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.child.Evaluate(GUI=False)
		self.Select()
		self.Print()


	def Spawn(self):
		self.child = copy.deepcopy(self.parent)

	def Mutate(self):
		self.child.Mutate()

	def Select(self):
		
		if self.parent.fitness < self.child.fitness :
			self.parent = self.child

	def Print(self):
		print("parent fitness :",self.parent.fitness," child fitness :",self.child.fitness)

	def SaveFitnessData(self):
		np.save('data/fitness_child.npy', self.fitnessOverTimeChild)
		np.save('data/fitness_parent.npy', self.fitnessOverTimeParent)