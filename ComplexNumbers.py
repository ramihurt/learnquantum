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

z_abs = abs(z)
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