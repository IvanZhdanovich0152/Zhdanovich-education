import numpy as np
from scipy.optimize import linprog

c = [-46, -2.3, -9.4, 0, 4]

A_ub = [
    [-3,   0,  -7.8, -12,  -9],
    [ 0, 2.3,   5,   5.6, -1],
    [-190, 98,  0,   4, -150]
]
b_ub = [-49, 86, -300]

A_eq = [[16, 0, 0, -40, 29]]
b_eq = [50]

bounds = [(0, None)] * 5

res = linprog(c, A_ub=A_ub, b_ub=b_ub,
              A_eq=A_eq, b_eq=b_eq,
              bounds=bounds, method="highs")

print(res.x)
print(-res.fun)

import pulp

prob = pulp.LpProblem("var5_max", pulp.LpMaximize)

x = pulp.LpVariable.dicts("x", range(1, 6), lowBound=0)

prob += 46*x[1] + 2.3*x[2] + 9.4*x[3] - 4*x[5]

prob += 3*x[1] + 7.8*x[3] + 12*x[4] + 9*x[5] >= 49
prob += 2.3*x[2] + 5*x[3] + 5.6*x[4] - x[5] <= 86
prob += 16*x[1] - 40*x[4] + 29*x[5] == 50
prob += 190*x[1] - 98*x[2] - 4*x[4] + 150*x[5] >= 300

prob.solve()

for i in range(1, 6):
    print(f"x{i} = {x[i].value()}")

print("f =", pulp.value(prob.objective))