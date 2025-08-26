import math
import cmath


x = -0.3415
y = 0.4282j

z = x + y
z_type = type(z)
print(f"Equation type: {z_type}")

x_squared = math.pow(-0.3415, 2)
y_squared = math.pow(0.4282, 2)

print(f"x_squared: {x_squared}")
print(f"y_squared: {y_squared}")
z_real = z.real
z_imag = z.imag

conjugate = z.conjugate()
# print(f"Real conjugation: {conjugate}")

# print(f"Real number {z_real} and imaginary number {z.imag}")

z_abs = abs(z) # square root of x^2 + y^2
print(f"Absolute value (magnitude) {z_abs}")

amplitude = cmath.phase(z)
print(f"Phase (amplitude) value {amplitude}")
print(f"Direction in degrees {math.degrees(amplitude)}")

y_over_x = z.imag / z.real
print(f"y_over_x value {y_over_x}")
result = math.atan(z.imag/z.real)  # Returns the arctan of x in radians
print(f"arctan result {result}")  # Output: 0.7853981633974483 (which is π/4)
degrees = math.degrees(result+math.pi)
print(f"phase in degrees {degrees}")

value = (-0.3415*2)+(0.4282*2)

print(value)
print(math.sqrt(value))
print(math.sqrt(0.3))
print(math.sqrt(0.7))

# The probability of an outcome is the square of the magnitude of its amplitude.

# The amplitude is described by the complex number

# The general steps are to calculate the magnitude and direction of an amplitude complex number,
# then calculate the probability of outcomes based on those numbers

# For more complex circuits:
# 1. Start with the initial state vector (all qubits in |0⟩)
# 2. Apply each gate in sequence (matrix multiplication)
# 3. The final state vector contains all the complex amplitudes

print(f"Probability of outcome 0 is {math.pow(0.55,2)}")
print(f"Probability of outcome 1 is {math.pow(0.84,2)}")
