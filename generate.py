import pyrosim.pyrosim as pyrosim

import random


def Create_World():

	pyrosim.Start_SDF("world.sdf")

	length= 1
	width= 1
	height = 1

	x= 5
	y = 3
	z = height/2

	pyrosim.Send_Cube(name="Box", pos=[x,y,z], size = [length,width,height])

	pyrosim.End()



def Create_Robot():
	pyrosim.Start_URDF("body.urdf")


	pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5], size = [1,1,1])

	pyrosim.Send_Joint(name="Torso_Leg_F", parent="Torso",child="LegFront", type="revolute",position="0.5 0 1")
	pyrosim.Send_Cube(name="LegFront", pos=[0.5,0,-.5], size = [1,1,1])

	pyrosim.Send_Joint(name="Torso_Leg_B", parent="Torso",child="LegBack", type="revolute",position="-0.5 0 1")
	pyrosim.Send_Cube(name="LegBack", pos=[-0.5,0,-.5], size = [1,1,1])

	pyrosim.End()

def generate_brain():

	pyrosim.Start_NeuralNetwork("brain.nndf")
	pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

	pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LegFront")

	pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LegBack")

	pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Leg_B")

	pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Leg_F")


	for sensor in range(3):
		for motor in range(2):
			pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor+3 , weight = (random.random()-0.5)*2 )


Create_World()
Create_Robot()

generate_brain()

