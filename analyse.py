import numpy as np
import matplotlib.pyplot as plt


backLegData = np.load("data/backLegSensorValues.npy")
frontLegData = np.load("data/frontLegSensorValues.npy")

plt.plot(backLegData)
plt.plot(frontLegData)
plt.show()