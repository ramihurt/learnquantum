import numpy as np
import matplotlib.pyplot as plt

# Create an array of values from -2π to 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calculate sine, cosine, and tangent
sin_x = np.sin(x)
cos_x = np.cos(x)
tan_x = np.tan(x)

# To avoid huge values near vertical asymptotes, limit tangent y-values
tan_x = np.where(np.abs(tan_x) > 10, np.nan, tan_x)

plt.figure(figsize=(12, 6))

# Plot sine
plt.plot(x, sin_x, label='sin(x)', color='blue')

# Plot cosine
plt.plot(x, cos_x, label='cos(x)', color='orange')

# Plot tangent
plt.plot(x, tan_x, label='tan(x)', color='green')

# Add vertical lines to indicate tangent asymptotes at odd multiples of π/2
for k in range(-3, 4):
    plt.axvline(x=(k + 0.5) * np.pi, color='red', linestyle='--', alpha=0.5)

plt.title('Graphs of sin(x), cos(x), and tan(x)')
plt.xlabel('x (radians)')
plt.ylabel('Function value')
plt.ylim(-5, 5)
plt.legend()
plt.grid(True)
plt.show()
