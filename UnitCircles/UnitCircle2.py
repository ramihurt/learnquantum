import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup
fig, (ax_circle, ax_wave) = plt.subplots(2, 1, figsize=(6, 8))

# Circle properties
theta = np.linspace(0, 2*np.pi, 500)
circle_x = np.cos(theta)
circle_y = np.sin(theta)

# Time values for the wave
t = np.linspace(0, 2*np.pi, 500)
sine_wave = np.sin(t)
cos_wave = np.cos(t)

# Draw the circle (static background)
ax_circle.plot(circle_x, circle_y, 'lightgray')
ax_circle.axhline(0, color='gray', lw=0.5)
ax_circle.axvline(0, color='gray', lw=0.5)
ax_circle.set_aspect('equal', 'box')
ax_circle.set_xlim(-1.2, 1.2)
ax_circle.set_ylim(-1.2, 1.2)
ax_circle.set_title("Unit Circle Projection")

# Initialize moving point and line
point, = ax_circle.plot([], [], 'ro')
line_proj_y, = ax_circle.plot([], [], 'b--', lw=1)

# Draw the sine wave (static background)
ax_wave.axhline(0, color='gray', lw=0.5)
ax_wave.set_xlim(0, 2*np.pi)
ax_wave.set_ylim(-1.2, 1.2)
ax_wave.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax_wave.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
ax_wave.set_title("Sine Wave from Y-Projection")

# Initialize sine plot
sine_line, = ax_wave.plot([], [], 'b')

# Animation update function
def update(frame):
    angle = t[frame]
    x = np.cos(angle)
    y = np.sin(angle)

    # Update point on circle
    point.set_data(x, y)
    line_proj_y.set_data([x, x], [0, y])

    # Update sine line up to current frame
    sine_line.set_data(t[:frame], sine_wave[:frame])

    return point, line_proj_y, sine_line

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=30, blit=True)

plt.tight_layout()
plt.show()