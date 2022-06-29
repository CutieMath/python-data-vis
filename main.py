import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

# Single Points basic
# ax = plt.axes(projection="3d")
# ax.scatter(3, 5, 7)
# plt.show()

# Single Points Scattered
# ax = plt.axes(projection="3d")
# x_data = np.random.randint(0, 100, (500, ))
# y_data = np.random.randint(0, 100, (500, ))
# z_data = np.random.randint(0, 100, (500, ))
# ax.scatter(x_data, y_data, z_data, alpha=0.1)
# plt.show()

# Single Points Function
ax = plt.axes(projection="3d")
x_data = np.arange(0, 50, 0.1)
y_data = np.arange(0, 50, 0.1)
z_data = np.sin(x_data) * np.cos(y_data)
ax.plot(x_data, y_data, z_data)
plt.show()

# Scatter Plots
