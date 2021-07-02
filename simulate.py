import sys

from simulation import SIMULATION

GUI = (sys.argv[1] == 'GUI')

solutionID = int(sys.argv[2])

simulation = SIMULATION(GUI,solutionID)

simulation.Run()

simulation.Get_Fitness()