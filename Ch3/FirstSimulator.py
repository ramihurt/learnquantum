from math import sqrt, atan2, pi, acos

from Ch3.util import is_close
from Ch3.sim_core import *
from Ch3.sim_gates import *
from random import choices
from collections import Counter

def to_table(s, decimals=5):
    table = [
        [k, s[k], atan2(s[k].imag, s[k].real) / (2 * pi) * 360, abs(s[k]),
         abs(s[k]) **2] for k in range(len(s))
    ]

    table_r = [[round(x, decimals) if isinstance(x, float) else round(x.real) + 1j * round(x.imag, decimals)
                if isinstance(x, complex) else x for x in table[k]] for k in range(len(table))]

    return table_r

def print_state(state, decimals=5):
    print(*to_table(state, decimals), sep='\n')

state = init_state()
print_state(state)

# Gates are used to modify amplitudes
# some gates change the outcome probabilities, some change the directions, and some change both


list = [0.2958+0.51235j, -0.40311+0.69821j]
state = prepare_state(*list)

state = [sqrt(0.3), -sqrt(0.7)]
print(state)

# 3.2.5 Single-qubit gate inverse

state = init_state()
state = [state[1], state[0]]
print(state)
state = [state[1], state[0]]
print(state)

# 3.3.3 Single-qubit circuits
state = init_state()
transform(state, ry(2*pi/3))
transform(state, x)
transform(state, phase(pi/3))
transform(state, h)
print_state(state) # different results than the example in the book

# 3.4 Simulating measurement of single-qubit system
samples = choices(range(len(state)), [abs(state[k])**2 for k in range(len(state))], k=10)
print(samples)
for (k, v) in Counter(samples).items():
    print(str(k) + ' -> ' + str(v))

samples = choices(range(len(state)), [abs(state[k])**2 for k in range(len(state))], k=1000)
for (k, v) in Counter(samples).items():
    print(str(k) + ' -> ' + str(v))

# 3.4.1 Encoding the uniform distribution in a single-qubit quantum state
state = init_state()
transform(state, h)
print_state(state)

samples = choices(range(len(state)), [abs(state[k])**2 for k in range(len(state))], k=1000)
for (k, v) in Counter(samples).items():
    print(str(k) + ' -> ' + str(v))

# 3.5.1
p = 0.7
theta = 2*acos(sqrt(p))
s = init_state()
transform(s, ry(theta))
print_state(s)

# 3.5.2
x = 273.5
theta = 2*acos(x/1000)
assert is_close(cos(theta/2), x/1000)
state = init_state()
transform(state, ry(theta))
print_state(state)