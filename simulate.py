import sys

from simulation import SIMULATION

GUI = (sys.argv[1] == 'GUI')

simulation = SIMULATION(GUI)

simulation.Run()

simulation.Get_Fitness()