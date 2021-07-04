import copy
import numpy as np
import os

from solution import SOLUTION
import constants as c


class PARALLEL_HILL_CLIMBER:

	def __init__(self):

		self.parents = {}
		self.NextAvailableID = 0

		os.system("rm brains/*")
		os.system("rm fitnesses/*")


		for individual in range(c.POPULATION_SIZE):
			self.parents[individual] = SOLUTION(self.NextAvailableID)

			self.NextAvailableID +=1 


	def Evolve(self):

		self.Evaluate(self.parents)

		for currentGeneration in range(c.NUMBER_OF_GENERATIONS):
			self.Evolve_For_One_Generation()

		
	def ShowBest(self):
		bestIndiv = max(self.parents.keys(),key = lambda indiv : self.parents[indiv].fitness)

		self.parents[bestIndiv].StartSimulation(GUI=True)

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()

		self.Evaluate(self.children)
		self.Print()
		self.Select()

	def Evaluate(self,solutions,GUI = False):

		for individual in solutions:
			solutions[individual].StartSimulation(GUI = GUI)

		for individual in solutions:
			solutions[individual].WaitSimToEnd()


	def Spawn(self):

		self.children = {}

		for individual in self.parents:
			self.children[individual] = copy.deepcopy(self.parents[individual])
			self.children[individual].Set_ID(self.NextAvailableID)
			self.NextAvailableID +=1

	def Mutate(self):
		for individual in self.parents:
			self.children[individual].Mutate()

	def Select(self):

		for individual in self.parents:
			if self.parents[individual].fitness < self.children[individual].fitness :
				self.parents[individual] = self.children[individual]

	def Print(self):
		print()
		print("parents : " + "	".join([str(indiv) + " : " + str(self.parents[indiv].fitness) for indiv in self.parents]))
		print("children : " + "	".join([str(indiv) + " : " + str(self.children[indiv].fitness) for indiv in self.children]))


	def SaveFitnessData(self):
		np.save('data/fitness_child.npy', self.fitnessOverTimeChild)
		np.save('data/fitness_parent.npy', self.fitnessOverTimeParent)