import numpy as np
import random
import os
import time

import pyrosim.pyrosim as pyrosim

import constants as c


class SOLUTION:
	def __init__(self,myID):

		self.myID = myID

		self.weight = 2*(np.random.rand(c.numSensorNeuron,c.numMotorNeuron)-0.5)

	def Mutate(self):
		randomCol = random.randint(0,c.numSensorNeuron-1)
		randomRow = random.randint(0,c.numMotorNeuron-1)

		self.weight[randomCol,randomRow] = random.random()*2-1

	def Evaluate(self,GUI = False):

		self.StartSimulation(GUI)

		self.WaitSimToEnd()

	def StartSimulation(self,GUI=False):
		self.Create_World()
		self.Create_Robot()
		self.generate_brain()

		os.system("python3 simulate.py "+ ("GUI " if GUI else "DIRECT ") +str(self.myID)+ " > /dev/null 2&>1 &")


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


		pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size = [1,1,0.5])

		#Front Leg
		pyrosim.Send_Joint(name="Torso_Leg_F", parent="Torso",child="LegFront", type="revolute",position="0 0.5 1",jointAxis='1 0 0')
		pyrosim.Send_Cube(name="LegFront", pos=[0,0.5,0], size = [0.2,1,0.2])

		pyrosim.Send_Joint(name="Leg_F_Leg_LF", parent="LegFront",child="LegLowerFront", type="revolute",position="0 1 0",jointAxis='0 1 0')
		pyrosim.Send_Cube(name="LegLowerFront", pos=[0,0,-0.5], size = [0.2,0.2,1])

		#Back Leg
		pyrosim.Send_Joint(name="Torso_Leg_B", parent="Torso",child="LegBack", type="revolute",position="0 -0.5 1",jointAxis='1 0 0')
		pyrosim.Send_Cube(name="LegBack", pos=[0,-0.5,0], size = [0.2,1,0.2])

		pyrosim.Send_Joint(name="Leg_B_Leg_LB", parent="LegBack",child="LegLowerBack", type="revolute",position="0 -1 0",jointAxis='0 1 0')
		pyrosim.Send_Cube(name="LegLowerBack", pos=[0,0,-0.5], size = [0.2,0.2,1])

		# Right Leg
		pyrosim.Send_Joint(name="Torso_Leg_R", parent="Torso",child="LegRight", type="revolute",position="0.5 0 1",jointAxis='0 1 0')
		pyrosim.Send_Cube(name="LegRight", pos=[0.5,0,0], size = [1,0.2,0.2])

		pyrosim.Send_Joint(name="Leg_R_Leg_LR", parent="LegRight",child="LegLowerRight", type="revolute",position="1 0 0",jointAxis='1 0 0')
		pyrosim.Send_Cube(name="LegLowerRight", pos=[0,0,-0.5], size = [0.2,0.2,1])

		# Left Leg
		pyrosim.Send_Joint(name="Torso_Leg_L", parent="Torso",child="LegLeft", type="revolute",position="-0.5 0 1",jointAxis='0 1 0')
		pyrosim.Send_Cube(name="LegLeft", pos=[-0.5,0,0], size = [1,0.2,0.2])

		pyrosim.Send_Joint(name="Leg_L_Leg_LL", parent="LegLeft",child="LegLowerLeft", type="revolute",position="-1 0 0",jointAxis='1 0 0')
		pyrosim.Send_Cube(name="LegLowerLeft", pos=[0,0,-0.5], size = [0.2,0.2,1])

		pyrosim.End()


	def generate_brain(self):

		pyrosim.Start_NeuralNetwork("brains/brain"+str(self.myID) +".nndf")

		linkNames = pyrosim.Get_Link_Names("body.urdf")
		SensorNames = [name for name in linkNames if "Lower" in name]

		jointNames = pyrosim.Get_Joint_Names("body.urdf")

		self.numSensorNeuron = len(SensorNames)
		self.numMotorNeuron = len(jointNames)


		NextAvailableName = 0

		for link in range(self.numSensorNeuron) :
			pyrosim.Send_Sensor_Neuron(name = NextAvailableName , linkName = SensorNames[link])
			NextAvailableName += 1

		for joint in range(self.numMotorNeuron) :

			pyrosim.Send_Motor_Neuron( name =NextAvailableName , jointName = jointNames[joint])
			NextAvailableName+=1


		for sensor in range(self.numSensorNeuron):
			for motor in range(self.numMotorNeuron):
				pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor+self.numSensorNeuron , weight = self.weight[sensor,motor] )

		pyrosim.End()