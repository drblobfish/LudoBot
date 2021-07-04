import os
from parallelhillclimber import PARALLEL_HILL_CLIMBER


phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()

phc.ShowBest()

'''
for i in range(5):
	os.system("python3 generate.py")
	os.system("python3 simulate.py")
'''