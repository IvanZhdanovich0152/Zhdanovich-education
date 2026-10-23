from scipy.optimize import linprog

c = [-108, -112, -126]

A_ub = [
    [0.8, 0.5, 0.6],
    [0.4, 0.4, 0.3],
    [0,   0.1, 0.1]
]
b_ub = [800, 600, 120]

bounds = [(0, None)] * 3

res = linprog(c, A_ub=A_ub, b_ub=b_ub,
              bounds=bounds, method="highs")

print(res.x)
print(-res.fun)