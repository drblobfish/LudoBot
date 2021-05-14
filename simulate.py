import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")
p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate("body.urdf")

while True:
	time.sleep(1/60)
	p.stepSimulation()

	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("LegBack")
	print(backLegTouch)


p.disconnect()