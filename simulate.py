import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random


NUMBER_STEP = 1000

AMPLITUDE = 0.8
FREQUENCY = 20
PHASE_OFFSET = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")
robot = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = np.zeros(NUMBER_STEP)
frontLegSensorValues = np.zeros(NUMBER_STEP)

targetAngle = AMPLITUDE * np.sin(FREQUENCY*np.linspace(-np.pi,np.pi,NUMBER_STEP)+PHASE_OFFSET)
np.save('data/targetAngle.npy',targetAngle)



for i in range(NUMBER_STEP):
	time.sleep(1/60)
	p.stepSimulation()

	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("LegBack")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("LegFront")


	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot,
		jointName = "Torso_Leg_B",
		controlMode = p.POSITION_CONTROL,
		targetPosition = targetAngle[i],
		maxForce = 100)

	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot,
		jointName = "Torso_Leg_F",
		controlMode = p.POSITION_CONTROL,
		targetPosition = targetAngle[i],
		maxForce = 100)


np.save('data/backLegSensorValues.npy',backLegSensorValues)
np.save('data/frontLegSensorValues.npy',frontLegSensorValues)

p.disconnect()