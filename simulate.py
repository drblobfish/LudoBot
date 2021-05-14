import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np


numberStep = 1000

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")
p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = np.zeros(numberStep)
frontLegSensorValues = np.zeros(numberStep)

for i in range(numberStep):
	time.sleep(1/60)
	p.stepSimulation()

	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("LegBack")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("LegFront")


np.save('data/backLegSensorValues.npy',backLegSensorValues)
np.save('data/frontLegSensorValues.npy',frontLegSensorValues)

p.disconnect()