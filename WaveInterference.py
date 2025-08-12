import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 500)
y1 = np.sin(t)
y2 = np.sin(t)  # phase = 0
y_sum = y1 + y2

plt.figure(figsize=(10, 4))
plt.plot(t, y1, label='Wave 1: sin(t)')
plt.plot(t, y2, label='Wave 2: sin(t + 0)')
plt.plot(t, y_sum, label='Sum', linewidth=2, color='black')
plt.title('Waves In Phase (Phase difference = 0)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

y2 = np.sin(t + np.pi)  # phase = pi
y_sum = y1 + y2

plt.figure(figsize=(10, 4))
plt.plot(t, y1, label='Wave 1: sin(t)')
plt.plot(t, y2, label='Wave 2: sin(t + π)')
plt.plot(t, y_sum, label='Sum', linewidth=2, color='black')
plt.title('Waves Out of Phase (Phase difference = π)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()