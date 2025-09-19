from math import sqrt, atan2, pi

from Ch3.util import is_close
from Ch3.sim_core import *

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