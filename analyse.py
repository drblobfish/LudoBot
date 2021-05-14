import numpy as np
import matplotlib.pyplot as plt


backLegData = np.load("data/backLegSensorValues.npy")
frontLegData = np.load("data/frontLegSensorValues.npy")

plt.plot(backLegData, label="back Leg Sensor",linewidth=3)
plt.plot(frontLegData, label="front Leg Sensor")
plt.legend()
plt.show()