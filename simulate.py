import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")
p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = np.zeros(1000)

for i in range(1000):
	time.sleep(1/60)
	p.stepSimulation()

	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("LegBack")


np.save('data/backLegSensorValues.npy',backLegSensorValues)

p.disconnect()