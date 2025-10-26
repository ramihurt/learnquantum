from math import sqrt, cos, sin, pi, atan2, log2, ceil, floor
import random
from util import is_close
from sim_gates import *

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

def cis(theta):
    return cos(theta) + 1j*sin(theta)

def is_power_of_two(m):
    return ceil(log2(m)) == floor(log2(m))

def prepare_state(*a):
    state = [a[k] for k in range(len(a))] # Checks that the length of the list is a power of 2
    assert(is_power_of_two(len(state)))
    assert (is_close(sum([abs(state[k]) ** 2 for k in range(len(state))]),
1.0))
    return state

def init_state(n):
    state = [0 for _ in range(2 ** n)] # Given n qubits, the state will contain 2n complex numbers.
    state[0] = 1 # The amplitude corresponding to outcome 0 (the first amplitude in the list) will have a value of 1.
    return state

def pair_generator_pattern(n, t):
    distance = int(2 ** t)
    for j in range(2 ** (n - t - 1)):
        for k0 in range(2 * j * distance, (2 * j + 1) * distance):
            k1 = k0 + distance
            yield k0, k1

def process_pair(state, gate, k0, k1):
    x = state[k0] # gets the original amplitudes of the pair
    y = state[k1]
    state[k0] = x * gate[0][0] + y * gate[0][1] # Computes the amplitudes given the gate definition
    state[k1] = x * gate[1][0] + y * gate[1][1] # and replaces the old amplitudes in the state list

def transform(state, t, gate):
    n = int(log2(len(state)))
    for (k0, k1) in pair_generator_pattern(n, t):
        process_pair(state, gate, k0, k1)

# Section 4.2
random.seed(123456789) # chose a seed to get reproducible results
probs = [random.random() for _ in range(4)] # Generates 4 random numbers
total = sum(probs)
probs = [p/total for p in probs] # Normalizes each amplitude so the probabilities add to 1

angles = [random.uniform(0, 2*pi) for _ in range(4)] # Generates four random angles in radians

state = [sqrt(p)*(cos(a) + 1j*sin(a)) for (p, a) in zip(probs, angles)] # build the quantum state list

print_state(state)
print()

p = 0.75
theta0 = 0
theta1 = 60/(180/pi)
first_state = [sqrt(p)*cis(theta0), sqrt(1-p)*cis(theta1)]
print([round(amp.real, 5)+1j*round(amp.imag, 5) for amp in first_state])

print()
q = 0.5
phi0 = 0
phi1 = -120/(180/pi)
second_state = [sqrt(q)*cis(phi0), sqrt(1-q)*cis(phi1)]
print([round(amp.real, 5)+1j*round(amp.imag, 5) for amp in second_state])

print()
new_state = [first_state[0]*second_state[0], first_state[0]*second_state[1],
first_state[1]*second_state[0], first_state[1]*second_state[1]]
print([round(amp.real, 5)+1j*round(amp.imag, 5) for amp in new_state])
print()

new_state = [sqrt(p*q)*cis(theta0 + phi0), sqrt(p*(1-q))*cis(theta0 + phi1),
sqrt((1-p)*q)*cis(theta1 + phi0), sqrt((1-p)*(1-q))*cis(theta1
+ phi1)]
print([round(amp.real, 5)+1j*round(amp.imag, 5) for amp in new_state])
print()

bell_state1 = [sqrt(0.5), 0.0, 0.0, sqrt(0.5)]
bell_state2 = [sqrt(0.5), 0.0, 0.0, -sqrt(0.5)]

print_state(bell_state1)
print()
print_state(bell_state2)
print()
bell_state3 = [0.0, sqrt(0.5), sqrt(0.5), 0.0]
bell_state4 = [0.0, sqrt(0.5), -sqrt(0.5), 0.0]
print_state(bell_state3)
print()
print_state(bell_state4)
print()

amplitude_list = [(0.09858+0.03637j), (0.07478+0.06912j), (0.04852+0.10526j), (0.00641+0.16322j), (-0.12895+0.34953j),
(0.58403-0.6318j), (0.18795-0.08665j), (0.12867-0.00506j)]

state = prepare_state(*amplitude_list)
print([[k, state[k]] for k in range(len(state))])
print()

print("probabilities and directions derived from amplitudes")
table1 = [
    [
        k,
        round(atan2(state[k].imag, state[k].real) / (2 * pi) * 360, 5),
        round(abs(state[k]) ** 2, 5)
    ]
    for k in range(len(state))
    ]
for row in table1:
    print(row)

print()

print("State table that includes the direction and magnitude of amplitudes, as well as the probability of the outcomes")
expanded_table = [
    [
        k,
        state[k],
        round(atan2(state[k].imag, state[k].real) / (2 * pi) * 360, 5),
        round(abs(state[k]), 5),
        round(abs(state[k]) ** 2, 5)
    ]
    for k in range(len(state))
]
for row in expanded_table:
    print(row)

print()
print("Initialize 2 qubit system")
state = init_state(2)
print(state)
print()

# Example pair generator
for (k0, k1) in pair_generator_pattern(3, 1):
    print(k0, k1)
print()

print("Applying X gate to target qubit 0 from our amplitude list")
transform(amplitude_list, 0, x) # Applies X gate to target qubit 0
print(amplitude_list)
print()

print("Applying X gate to target qubit 2 from our amplitude list")
transform(amplitude_list, 2, x) # Applies X gate to target qubit 0
print(amplitude_list)
print()