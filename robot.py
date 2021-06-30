import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK


import constants as c

import numpy as np
import random

from sensor import SENSOR
from motor import MOTOR



class ROBOT:
	def __init__(self):

		self.robot = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate("body.urdf")
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		self.nn = NEURAL_NETWORK("brain.nndf")

	
	def Get_Fitness(self):
		self.stateOfLink0 = p.getLinkState(self.robot,0)
		self.position0fLink0 = self.stateOfLink0[0]
		self.xCoordOfLink0 = self.position0fLink0[0]

		with open('fitness.txt','w') as fitnessFile :
			fitnessFile.write(str(self.xCoordOfLink0))
		

	def Prepare_To_Sense(self):
		self.sensors={}

		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Prepare_To_Act(self):
		self.motors = {}

		for jointName in pyrosim.jointNamesToIndices:
			if jointName == 'Torso_Leg_B':
				self.motors[jointName] = MOTOR(jointName,frequency=c.FREQUENCY/2)
			else:
				self.motors[jointName] = MOTOR(jointName)



	def Sense(self,t):

		for sensor in self.sensors:
			self.sensors[sensor].Get_Value(t)

	def Think(self,t):
		self.nn.Update()
		#self.nn.Print()

	def Act(self,t):

		for neuron in self.nn.Get_Motor_Neuron():
			jointName = self.nn.Get_Neuron_Joint(neuron)
			desiredAngle = self.nn.Get_Value_Of(neuron)
			
			self.motors[jointName].Set_Value(self.robot,desiredAngle)

	def print_sensors(self):
		for sensor in self.sensors:
			self.sensors[sensor].print_values()

	def save_sensors(self):
		for sensor in self.sensors:
			self.sensors[sensor].save_values()

	def print_motors(self):
		for jointName in self.motors:
			self.motors[jointName].print_values()

	def save_motors(self):
		for jointName in self.motors:
			self.motors[jointName].save_values()