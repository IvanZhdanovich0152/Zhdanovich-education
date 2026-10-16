import numpy as np

N, F = 4, 8
n = N + F

# Задание 1
i = np.arange(1, n + 1)
x = (i - 1) / (i + 1) + np.sin((i - 1) ** 2)

print("Массив х:")
print(x)

sum_x = np.sum(x)
prod_x = np.prod(x)
mean_x = np.mean(x)
var_x = np.var(x)
std_x = np.std(x)
min_x = np.min(x)
max_x = np.max(x)
argmin_x = np.argmin(x)
argmax_x = np.argmax(x)

print(f"1. Сумма:                  {sum_x:.6f}")
print(f"2. Произведение:           {prod_x:.6f}")
print(f"3. Среднее:                {mean_x:.6f}")
print(f"4. Дисперсия:              {var_x:.6f}")
print(f"5. Ст. отклонение:         {std_x:.6f}")
print(f"6. Минимум:                {min_x:.6f}")
print(f"7. Максимум:               {max_x:.6f}")
print(f"8. Индекс минимума:        {argmin_x}")
print(f"9. Индекс максимума:       {argmax_x}")

m = 3
A = x[:m*m].reshape(m, m)
print("Матрица A (3×3):")
print(A)

first_row = A[0, :]
last_col  = A[:, -1]
dot_prod  = np.dot(first_row, last_col)

print("Первая строка:      ", first_row)
print("Последний столбец:  ", last_col)
print(f"Скалярное произведение: {dot_prod:.6f}")

v1 = A[0, :3]
v2 = A[-1, :3]
cross_prod = np.cross(v1, v2)

print("v1 =", v1)
print("v2 =", v2)
print("Векторное произведение:", cross_prod)

# Задание 2

B = np.zeros((n, n))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i <= j:
            B[i-1, j-1] = max(np.sin(i), np.cos(j))
        else:
            B[i-1, j-1] = 0.4 * i**2 + 0.3 * np.sin(j)

np.set_printoptions(precision=4, suppress=True)
print("Матрица  B (12×12):")
print(B)

row_sums = np.sum(B, axis=1)
print("Суммы по строкам:", row_sums)

col_sums = np.sum(B, axis=0)
print("Суммы по столбцам:", col_sums)

B_inv = np.linalg.inv(B)
check = B @ B_inv
print("Обратная матрица (первые 3×3):")
print(B_inv[:3, :3])
print("\nПроверка B @ B_inv (должна быть E):")
print(np.round(check, 10))

det_B   = np.linalg.det(B)
rank_B  = np.linalg.matrix_rank(B)
trace_B = np.trace(B)

print(f"Определитель: {det_B:.6f}")
print(f"Ранг:         {rank_B}")
print(f"След:         {trace_B:.6f}")


eigvals, eigvecs = np.linalg.eig(B)

print("Собственные значения:")
print(eigvals)

alpha = eigvals[0]
v = eigvecs[:, 0]
print("\nПроверка B @ v - alpha * v (должно быть ≈ 0):")
print(B @ v - alpha * v)

try:
    L = np.linalg.cholesky(B)
    print("Матрица L (Холецкий):")
    print(L)
    print("\nПроверка L @ L.T:")
    print(np.round(L @ L.T, 6))
except np.linalg.LinAlgError:
    print("Матрица не является положительно определённой — разложение Холецкого невозможно.")


Q, R = np.linalg.qr(B)
print("Q (ортогональная):")
print(Q)
print("\nR (верхнетреугольная):")
print(R)
print("\nПроверка Q @ R:")
print(np.round(Q @ R, 6))


U, S, Vt = np.linalg.svd(B)
print("Сингулярные числа:", S)
print("\nU:", U.shape, " S:", S.shape, " Vt:", Vt.shape)
print("\nПроверка U @ diag(S) @ Vt:")
Sigma = np.zeros((n, n))
np.fill_diagonal(Sigma, S)
print(np.round(U @ Sigma @ Vt, 6))


norm_1   = np.linalg.norm(B, 1)
norm_2   = np.linalg.norm(B, 2)
norm_inf = np.linalg.norm(B, np.inf)
norm_fro = np.linalg.norm(B, 'fro')

cond_1   = np.linalg.cond(B, 1)
cond_2   = np.linalg.cond(B, 2)
cond_inf = np.linalg.cond(B, np.inf)

print(f"||B||_1   = {norm_1:.4f}")
print(f"||B||_2   = {norm_2:.4f}")
print(f"||B||_inf = {norm_inf:.4f}")
print(f"||B||_F   = {norm_fro:.4f}")
print(f"cond_1(B)   = {cond_1:.4f}")
print(f"cond_2(B)   = {cond_2:.4f}")
print(f"cond_inf(B) = {cond_inf:.4f}")

half = n // 2
B_half = B[:half, :half]
print("Матрица B_half (6×6):")
print(B_half)


# Задание 3

C_sys = np.array([
    [5.0,  0.8, -1.8,   1.0],
    [2.0, -5.0,  1.0,  -2.0],
    [3.0,  2.0, -8.0,   2.0],
    [2.0, -4.0,  5.0, -12.0]
])
D = np.array([0.4, -2.0, -2.0, 6.0])

X_matrix = np.linalg.inv(C_sys) @ D
print("Решение матричным методом:", X_matrix)
print("Проверка A @ X - B:", C_sys @ X_matrix - D)

X_solve      = np.linalg.solve(C_sys, D)
X_lstsq      = np.linalg.lstsq(C_sys, D, rcond=None)[0]
X_tensorsolve = np.linalg.tensorsolve(C_sys, D)

print("solve:      ", X_solve)
print("lstsq:      ", X_lstsq)
print("tensorsolve:", X_tensorsolve)

for name, X in [("matrix", X_matrix), ("solve", X_solve),
                ("lstsq", X_lstsq), ("tensorsolve", X_tensorsolve)]:
    residual = A_sys @ X - B
    print(f"{name:12s} → невязка: {np.max(np.abs(residual)):.2e}")



