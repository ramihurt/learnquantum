import sys
sys.path.insert(0,'..')

from apps.knapsack import solve_knapsack

values = [2, 3, 1]
weights = [3, 2, 1]
max_weight = 4

solve_knapsack(values, weights, max_weight)