import numpy as np
import matplotlib.pyplot as plt


backLegData = np.load("data/backLegSensorValues.npy")

plt.plot(backLegData)
plt.show()