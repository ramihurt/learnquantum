# Chapter 3, section 3.1.3
from math import sqrt
from math import atan2
from math import pi
from math import cos, sin

state = [0.2958+0.51235j, -0.40311+0.69821j]

# Print the amplitude for outcome 0 in a single qubit system
print(f"Amplitude for outcome 0: {state[0]} \n")

# These example states have positive real numbers as amplitudes (the imaginary part is 0).
# If an amplitude is a positive real number, its direction must be a 0 angle.
state1 = [1, 0]
state2 = [0, 1]
state3 = [sqrt(1/2), sqrt(1/2)]
state4 = [sqrt(0.3), sqrt(0.7)]

state = [1, 0]
print(f"State 0 real number: {state[0].real} and state 0 imaginary number {state[0].imag} \n")

# To verify that the previous examples are valid single-qubit quantum states, we can
# check that the sum of the squared magnitudes is 1

state = [1, 0]
assert sum([abs(k)**2 for k in state]) == 1
state1 = [sqrt(0.3), sqrt(0.7)]
assert sum([abs(k)**2 for k in state1]) == 1

# The following state shows an example of an amplitude that is a negative real number,
# whose direction is 180°, or π radians:
state = [sqrt(0.3), -sqrt(0.7)]
direction = atan2(state[1].imag, state[1].real)
print(f"direction for an amplitude that is a negative real number, "
      f"whose direction is 180°, or π radians): {direction} \n")

# We can convert from radians to degrees with the following expression
print(f"convert from radians to degrees: {direction * (180/pi)} \n")

# The following is a state with amplitude directions π/7 and π/5 radians
state = [sqrt(0.3) * (cos(5 * pi / 7) + 1j * sin(5 * pi / 7)),
 sqrt(0.7) * (cos(pi / 5) + 1j * sin(pi / 5))]
print(f"The following is a state with amplitude directions π/7 and π/5 radians")
print(f"{state} \n")

# Although this list is an efficient, compact representation, it is useful to explicitly
# include each index (which is the same as the outcome in this representation)
table = [[k, state[k]] for k in range(len(state))]
print(f"explicitly include each index")
for row in table:
 print(row)
print("")

# To make the table more readable, we can use fewer decimal places for the real and
# imaginary parts of the amplitudes. For example, let’s format them using five digits
# after the decimal point:
print("use fewer decimal places for the real and imaginary parts of the amplitudes")
formatted_table = [
 [
 round(x.real, 5) + 1j * round(x.imag, 5) if isinstance(x, complex) else x
 for x in table[k]
 ]
 for k in range(len(table))
]
for row in formatted_table:
 print(row)
print("")

# Next, we will add the other properties we want in the state table: direction, magnitude, and probability.
# We can get the magnitude of a complex number using the built-in Python function abs:
print(f"To get the magnitude, use absolute value function of the complex number")
print(f"abs(state[0]: {abs(state[0])}\n")

# To get the probability, we square the magnitude:
print(f"To get the probability, we square the magnitude")
print(f"abs(state[0])**2: {abs(state[0])**2}\n")
abs(state[0])**2

# Put all together
print("Put it all together")
expanded_table = [
 [
 k,
 state[k],
 atan2(state[k].imag, state[k].real) * (180 / pi),
 abs(state[k]),
 abs(state[k]) ** 2
 ]
 for k in range(len(state))
]
formatted_expanded_table = [
 [
 round(x, 5) if isinstance(x, float)
 else round(x.real, 5) + 1j * round(x.imag, 5) if isinstance(x, complex)
 else x
 for x in expanded_table[k]
 ]
 for k in range(len(expanded_table))
]

for row in formatted_expanded_table:
 print(row)
