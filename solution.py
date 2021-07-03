import numpy as np
import random
import os
import time

import pyrosim.pyrosim as pyrosim


class SOLUTION:
	def __init__(self,myID):

		self.myID = myID

		self.weight = 2*(np.random.rand(3,2)-0.5)

	def Mutate(self):
		randomCol = random.randint(0,2)
		randomRow = random.randint(0,1)

		self.weight[randomCol,randomRow] = random.random()*2-1

	def Evaluate(self,GUI = False):

		self.StartSimulation(GUI)

		self.WaitSimToEnd()

	def StartSimulation(self,GUI=False):
		self.Create_World()
		self.Create_Robot()
		self.generate_brain()

		os.system("python3 simulate.py "+ ("GUI " if GUI else "DIRECT ") +str(self.myID)+ " &")


	def WaitSimToEnd(self):

		self.fitnessFilePATH = "fitnesses/fitness"+str(self.myID)+".txt"
		
		while not os.path.exists(self.fitnessFilePATH):
			time.sleep(0.01)

		with open(self.fitnessFilePATH,"r") as fitnessfile :
			self.fitness = float(fitnessfile.read())

		os.system("rm "+ self.fitnessFilePATH)


	def Set_ID(self,ID):
		self.myID = ID

	def Create_World(self):

		pyrosim.Start_SDF("world.sdf")

		length= 1
		width= 1
		height = 1

		x= 5
		y = 3
		z = height/2

		pyrosim.Send_Cube(name="Box", pos=[x,y,z], size = [length,width,height])

		pyrosim.End()

	def Create_Robot(self):
		pyrosim.Start_URDF("body.urdf")


		pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5], size = [1,1,1])

		pyrosim.Send_Joint(name="Torso_Leg_F", parent="Torso",child="LegFront", type="revolute",position="0.5 0 1")
		pyrosim.Send_Cube(name="LegFront", pos=[0.5,0,-.5], size = [1,1,1])

		pyrosim.Send_Joint(name="Torso_Leg_B", parent="Torso",child="LegBack", type="revolute",position="-0.5 0 1")
		pyrosim.Send_Cube(name="LegBack", pos=[-0.5,0,-.5], size = [1,1,1])

		pyrosim.End()


	def generate_brain(self):

		pyrosim.Start_NeuralNetwork("brains/brain"+str(self.myID) +".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LegFront")

		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LegBack")

		pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Leg_B")

		pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Leg_F")


		for sensor in range(3):
			for motor in range(2):
				pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor+3 , weight = self.weight[sensor,motor] )

		pyrosim.End()