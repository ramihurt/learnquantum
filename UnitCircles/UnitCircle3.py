


import numpy as np
import matplotlib.pyplot as plt

# Time settings
t = np.linspace(0, 1, 500)  # 1 second, 500 points
frequency = 3  # 3 Hz tone (3 cycles per second)
omega = 2 * np.pi * frequency

# Circular motion
x_circle = np.cos(omega * t)
y_circle = np.sin(omega * t)

# Sound wave (sine projection)
sound_wave = y_circle

# Create the figure
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: Unit Circle
axes[0].plot(x_circle, y_circle, label='Circular Motion')
axes[0].scatter([x_circle[0]], [y_circle[0]], color='red', label='Start Point')
axes[0].set_title("Unit Circle (Circular Motion)")
axes[0].set_xlabel("X (cos θ)")
axes[0].set_ylabel("Y (sin θ)")
axes[0].set_aspect('equal', adjustable='box')
axes[0].grid(True)
axes[0].legend()

# Right: Sound Wave
axes[1].plot(t, sound_wave, label='Sound Wave (sin θ)')
axes[1].set_title("Sound Wave Over Time")
axes[1].set_xlabel("Time (seconds)")
axes[1].set_ylabel("Amplitude (Pressure Variation)")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()
