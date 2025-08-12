import math
import cmath

z = 0.2 + 0.3j
z_type = type(z)
print(f"Equation type: {z_type}")
z_real = z.real
z_imag = z.imag

conjugate = z.conjugate()
print(f"Real conjugation: {conjugate}")

print(f"Real number {z_real} and imaginary number {z.imag}")

z_abs = abs(z)
print(f"Absolute value (magnitude) {z_abs}")

amplitude = cmath.phase(z)
print(f"Phase value {amplitude}")

value = (-0.3415*2)+(0.4282*2)

print(value)
print(math.sqrt(value))
print(math.sqrt(0.3))
print(math.sqrt(0.7))