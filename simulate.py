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
robot = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = np.zeros(numberStep)
frontLegSensorValues = np.zeros(numberStep)

for i in range(numberStep):
	time.sleep(1/60)
	p.stepSimulation()

	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("LegBack")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("LegFront")

	targetPosB = 0 if pyrosim.Get_Touch_Sensor_Value_For_Link("LegBack")==-1 else -np.pi/4
	targetPosF = 0 if pyrosim.Get_Touch_Sensor_Value_For_Link("LegFront")==-1 else np.pi/4


	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot,
		jointName = "Torso_Leg_B",
		controlMode = p.POSITION_CONTROL,
		targetPosition = targetPosB,
		maxForce = 500)

	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robot,
		jointName = "Torso_Leg_F",
		controlMode = p.POSITION_CONTROL,
		targetPosition = targetPosF,
		maxForce = 500)


np.save('data/backLegSensorValues.npy',backLegSensorValues)
np.save('data/frontLegSensorValues.npy',frontLegSensorValues)

p.disconnect()