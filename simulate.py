import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random


NUMBER_STEP = 1000

AMPLITUDE_FRONT = 0.5
FREQUENCY_FRONT = 10
PHASE_OFFSET_FRONT = 0

AMPLITUDE_BACK = 0.5
FREQUENCY_BACK = 20
PHASE_OFFSET_BACK = -np.pi/5

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")
robot = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = np.zeros(NUMBER_STEP)
frontLegSensorValues = np.zeros(NUMBER_STEP)

targetAngleFront = AMPLITUDE_FRONT * np.sin(FREQUENCY_FRONT*(np.linspace(-np.pi,np.pi,NUMBER_STEP)+PHASE_OFFSET_FRONT))
np.save('data/targetAngleFront.npy',targetAngleFront)

targetAngleBack = AMPLITUDE_BACK * np.sin(FREQUENCY_BACK*(np.linspace(-np.pi,np.pi,NUMBER_STEP)+PHASE_OFFSET_BACK))
np.save('data/targetAngleBack.npy',targetAngleBack)


for i in range(NUMBER_STEP):
	time.sleep(1/60)
	p.stepSimulation()

	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("LegBack")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("LegFront")


	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot,
		jointName = "Torso_Leg_B",
		controlMode = p.POSITION_CONTROL,
		targetPosition = targetAngleBack[i],
		maxForce = 100)

	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot,
		jointName = "Torso_Leg_F",
		controlMode = p.POSITION_CONTROL,
		targetPosition = targetAngleFront[i],
		maxForce = 100)


np.save('data/backLegSensorValues.npy',backLegSensorValues)
np.save('data/frontLegSensorValues.npy',frontLegSensorValues)

p.disconnect()