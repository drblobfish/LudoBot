import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim


import numpy as np
import random
import time

import constants as c
from world import WORLD
from robot import ROBOT


class SIMULATION:
	def __init__(self):

		self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())

		p.setGravity(0,0,-9.8)


		self.world = WORLD()
		self.robot = ROBOT()

	def Run(self):

		for t in range(c.NUMBER_STEP):

			time.sleep(1/60)
			p.stepSimulation()

			self.robot.Sense(t)
			self.robot.Think(t)
			self.robot.Act(t)

	def __del__(self):
		p.disconnect()
		'''
		self.robot.print_sensors()
		self.robot.print_motors()


		self.robot.save_sensors()
		self.robot.save_motors()
		'''