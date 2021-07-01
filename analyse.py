import numpy as np
import matplotlib.pyplot as plt


#backLegData = np.load("data/backLegSensorValues.npy")
#frontLegData = np.load("data/frontLegSensorValues.npy")

#targetDataBack = np.load("data/targetAngleBack.npy")
#targetDataFront = np.load("data/targetAngleFront.npy")

fitnesschild = np.load("data/fitness_child.npy")
fitnessparent = np.load("data/fitness_parent.npy")


#plt.plot(backLegData, label="back Leg Sensor",linewidth=3)
#plt.plot(frontLegData, label="front Leg Sensor")
#plt.plot(targetDataBack,label="targetDataBack")
#plt.plot(targetDataFront,label="targetDataFront")

plt.plot(fitnesschild,label="fitness child")
plt.plot(fitnessparent,label="fitness parent")


plt.legend()
plt.show()