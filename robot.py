import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

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

	def Act(self,t):

		for jointName in self.motors:
			self.motors[jointName].Set_Value(self.robot,t)

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