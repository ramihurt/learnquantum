from util import is_close

# The default state for a qubit system is one where the only possible outcome is a 0 for each qubit.
# The probability of getting a 0 is 100%
def init_state():
    state = [0 for _ in range(2)]
    state[0] = 1
    return state

# Gates are used to modify amplitudes
# some gates change the outcome probabilities, some change the directions, and some change both

def prepare_state(*a):
    state = [a[k] for k in range(len(a))]
    assert(len(state) == 2)
    assert(is_close(sum([abs(state[k])**2 for k in range(len(state))]), 1))
    return state


def transform(state, gate):
    assert(len(state) == 2)
    z0 = state[0]
    z1 = state[1]
    state[0] = gate[0][0]*z0 + gate[0][1]*z1
    state[1] = gate[1][0]*z0 + gate[1][1]*z1
