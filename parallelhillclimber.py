import copy
import numpy as np

from solution import SOLUTION
import constants as c


class PARALLEL_HILL_CLIMBER:

	def __init__(self):

		self.parents = {}
		self.NextAvailableID = 0

		for individual in range(c.POPULATION_SIZE):
			self.parents[individual] = SOLUTION(self.NextAvailableID)

			self.NextAvailableID +=1 

		#print(self.parents)

	def Evolve(self):
		
		for individual in self.parents:
			self.parents[individual].Evaluate(GUI=True)

		
	def ShowBest(self):
		pass

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.child.Evaluate(GUI=False)
		self.Select()
		self.Print()


	def Spawn(self):
		self.child = copy.deepcopy(self.parent)
		self.child.Set_ID(self.NextAvailableID)
		self.NextAvailableID += 1

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