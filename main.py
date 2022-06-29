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
# ax = plt.axes(projection="3d")
# x_data = np.arange(0, 50, 0.1)
# y_data = np.arange(0, 50, 0.1)
# z_data = np.sin(x_data) * np.cos(y_data)
# ax.plot(x_data, y_data, z_data)
# ax.set_title("Cutie plot")
# ax.set_xlabel("X value label (cm)")
# ax.set_ylabel("Y value label (cm)")
# ax.set_zlabel("Z value label (cm)")
# plt.show()

# Surface Plots (mesh grid)
# ax = plt.axes(projection="3d")
# x_data = np.arange(0, 50, 0.1)
# y_data = np.arange(0, 50, 0.5)
# X, Y = np.meshgrid(x_data, y_data)
# print(X)
#
# Z = X * Y
# ax.plot_surface(X, Y, Z)
# plt.show()

# Surface Plots
ax = plt.axes(projection="3d")
x_data = np.arange(-5, 5, 0.1)
y_data = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x_data, y_data)
print(X)

Z = np.sin(X) * np.cos(Y)
ax.plot_surface(X, Y, Z, cmap="plasma")
# Add default value for initial position
# azimuth = 0, elevation of 90
ax.view_init(azim=0, elev=90)
plt.show()


