from Ch3.util import is_close

# The default state for a qubit system is one where the only possible outcome is a 0 for each qubit.
# The probability of getting a 0 is 100%

def init_state():
    state = [0 for _ in range(2)]
    state[0] = 1
    return state

state = init_state()
print(state)

# Gates are used to modify amplitudes

def prepare_state(*a):
    state = [a[k] for k in range(len(a))]
    # Checks that the state has two amplitudes
    assert(len(state) == 2)
    assert(is_close(sum([abs(state[k])**2 for k in range(len(state))]), 1))
    return state

list = [0.2958+0.51235j, -0.40311+0.69821j]
state = prepare_state(*list)