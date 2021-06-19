import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

import constants as c

import numpy as np
import random


class SENSOR:
	def __init__(self,linkName):
		self.linkName = linkName
		self.Prepare_To_Sense()

	def Prepare_To_Sense(self):
		self.values = np.zeros(c.NUMBER_STEP)

	def Get_Value(self,t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

	def print_values(self):
		print(self.linkName,self.values)

	def save_values(self):
		np.save('data/'+self.linkName +'SensorValues.npy',self.values)