import math
import cmath

z = -0.34 + 0.43j
z_type = type(z)
z_real = z.real
z_imag = z.imag

conjugate = z.conjugate()
print(f"Real conjugation: {conjugate}")

print(f"Real number {z_real} and imaginary number {z.imag}")

z_abs = abs(z) # square root of x^2 + y^2
print(f"Absolute value (magnitude) {z_abs}")

amplitude = cmath.phase(z) # arctan(y/x)
print(f"Phase value in radians {amplitude}")
print(f"Phase value in degrees {math.degrees(amplitude)}")

value = (-0.3415*2)+(0.4282*2)

print(value)
print(math.sqrt(value))
print(math.sqrt(0.3))
print(math.sqrt(0.7))

# The probability of an outcome is the square of the magnitude of its amplitude.
# The amplitude is described by the complex number
# The general steps are to calculate the magnitude and direction of an amplitude complex number,
# then calculate the probability of outcomes based on those numbers

print(f"Probability of outcome 0 is {math.pow(0.55,2)}")
print(f"Probability of outcome 1 is {math.pow(0.84,2)}")
