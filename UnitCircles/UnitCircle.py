import numpy as np
import matplotlib.pyplot as plt

# Create the circle
theta = np.linspace(0, 2*np.pi, 500)
x = np.cos(theta)
y = np.sin(theta)

# Key angles in radians and their labels
angles = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2,
          2*np.pi/3, 3*np.pi/4, 5*np.pi/6, np.pi,
          7*np.pi/6, 5*np.pi/4, 4*np.pi/3, 3*np.pi/2,
          5*np.pi/3, 7*np.pi/4, 11*np.pi/6]
labels = ["0", "π/6", "π/4", "π/3", "π/2",
          "2π/3", "3π/4", "5π/6", "π",
          "7π/6", "5π/4", "4π/3", "3π/2",
          "5π/3", "7π/4", "11π/6"]

# Plot the unit circle
plt.figure(figsize=(7,7))
plt.plot(x, y, 'b')  # unit circle
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)

# Plot and label key points
for angle, label in zip(angles, labels):
    px, py = np.cos(angle), np.sin(angle)
    plt.plot(px, py, 'ro')
    plt.text(px*1.1, py*1.1, label, ha='center', va='center', fontsize=9)

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Unit Circle with Key Angles", fontsize=14)
plt.xlabel("cos(θ) (x-coordinate)")
plt.ylabel("sin(θ) (y-coordinate)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
