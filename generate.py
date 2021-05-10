import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length= 1
width= 2
height = 3

x= 0
y = 0
z = height/2

pyrosim.Send_Cube(name="Box1", pos=[x,y,z], size = [length,width,height])

pyrosim.Send_Cube(name="Box2", pos=[x+length,y+width,z+height], size = [length,width,height])

pyrosim.End()