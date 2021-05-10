import pyrosim.pyrosim as pyrosim


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


Create_World()
Create_Robot()