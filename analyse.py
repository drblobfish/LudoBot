import numpy as np
import matplotlib.pyplot as plt


backLegData = np.load("data/backLegSensorValues.npy")
frontLegData = np.load("data/frontLegSensorValues.npy")

targetDataBack = np.load("data/targetAngleBack.npy")
targetDataFront = np.load("data/targetAngleFront.npy")


#plt.plot(backLegData, label="back Leg Sensor",linewidth=3)
#plt.plot(frontLegData, label="front Leg Sensor")
plt.plot(targetDataBack,label="targetDataBack")
plt.plot(targetDataFront,label="targetDataFront")

plt.legend()
plt.show()