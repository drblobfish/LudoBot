import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length= 1
width= 3
height = 1

x= 0
y = 0
z = height/2

hauteur_tour = 10

current_height = 0

for i in range(hauteur_tour):
	pyrosim.Send_Cube(name="Box"+str(i), pos=[x,y,current_height+height * (0.9**i)/2], size = [length * (0.9**i),width * (0.9**i),height * (0.9**i)])
	#print(current_height)
	current_height+=height * (0.9**(i))

pyrosim.End()