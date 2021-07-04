import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

import constants as c

import numpy as np
import random


class MOTOR:
	def __init__(self,jointName,amplitude = c.AMPLITUDE, frequency=c.FREQUENCY, phase_offset = c.PHASE_OFFSET):


		self.amplitude = amplitude
		self.frequency = frequency
		self.phase_offset = phase_offset

		self.jointName = jointName
		#self.Prepare_To_Act()

	def Prepare_To_Act(self):

		self.MotorValues = self.amplitude * np.sin(self.frequency*(np.linspace(-np.pi,np.pi,c.NUMBER_STEP)+self.phase_offset))

	def Set_Value(self,robot,desiredAngle):
		pyrosim.Set_Motor_For_Joint(
				bodyIndex = robot,
				jointName = self.jointName,
				controlMode = p.POSITION_CONTROL,
				targetPosition = desiredAngle,
				maxForce = 100)

	def print_values(self):
		print(self.jointName,self.MotorValues)

	def save_values(self):
		np.save('data/'+self.jointName +'MotorsValues.npy',self.MotorValues)