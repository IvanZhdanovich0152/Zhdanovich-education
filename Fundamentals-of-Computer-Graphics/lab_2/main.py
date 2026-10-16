import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

P = np.array([
    [2, 2, 5],
    [6, 9, 7],
    [5, 4, 3],
    [1, 2, 9]
], dtype=float)

def natural_cubic_spline(y):
    n = len(y) - 1
    h = 1.0

    A = np.zeros((n-1, n-1))
    rightSide = np.zeros(n-1)
    for i in range(1, n):
        if i-1 > 0: A[i-1, i-2] = h/6
        A[i-1, i-1] = 2*h/3
        if i < n-1: A[i-1, i] = h/6
        rightSide[i-1] = (y[i+1] - 2*y[i] + y[i-1]) / h

    M_inner = np.linalg.solve(A, rightSide)
    M = np.concatenate(([0.0], M_inner, [0.0]))

    coeffs = []
    for i in range(n):
        a = (M[i+1] - M[i]) / (6*h)
        b = M[i] / 2
        c = (y[i+1] - y[i])/h - h*(2*M[i] + M[i+1])/6
        d = y[i]
        coeffs.append((a, b, c, d))
    return coeffs

def bezier_from_poly(a, b, c, d):
    P0 = d
    P1 = d + c/3
    P2 = (a+b+c+d) - (3*a + 2*b + c)/3
    P3 = a + b + c + d
    return np.array([P0, P1, P2, P3])

coeffs_x = natural_cubic_spline(P[:,0])
coeffs_y = natural_cubic_spline(P[:,1])
coeffs_z = natural_cubic_spline(P[:,2])

segments = []
for i in range(3):
    bx = bezier_from_poly(*coeffs_x[i])
    by = bezier_from_poly(*coeffs_y[i])
    bz = bezier_from_poly(*coeffs_z[i])
    seg = np.stack([bx, by, bz], axis=1)
    segments.append(seg)

fig = plt.figure(figsize=(12, 10))

ax_xy = fig.add_subplot(2, 2, 1)
ax_yz = fig.add_subplot(2, 2, 2)
ax_xz = fig.add_subplot(2, 2, 3)

def plot_projection(
        ax,
        seg_list,
        P,
        idx_h,
        idx_v,
        title
    ):
    colors = ['red', 'green', 'blue']
    for i, seg in enumerate(seg_list):
        t = np.linspace(0, 1, 200)

        B = ((1-t)**3)[:,None]*seg[0] + (3*(1-t)**2*t)[:,None]*seg[1] \
          + (3*(1-t)*t**2)[:,None]*seg[2] + (t**3)[:,None]*seg[3]

        ax.plot(B[:, idx_h], B[:, idx_v], color=colors[i], lw=2, label=f'Сегмент {i+1}')

        hull = np.vstack([seg, seg[0]])

        ax.plot(hull[:, idx_h], hull[:, idx_v], '--', color=colors[i], alpha=0.5)
        ax.scatter(seg[:, idx_h], seg[:, idx_v], color=colors[i], s=30)

    ax.scatter(P[:, idx_h], P[:, idx_v], color='black', s=80, marker='s', zorder=5, label='Опорные точки')

    for j, p in enumerate(P):
        ax.annotate(f'P{j}', (p[idx_h], p[idx_v]), textcoords="offset points", xytext=(5,5), fontsize=9)

    ax.set_xlabel(f'Координата {["X","Y","Z"][idx_h]}')
    ax.set_ylabel(f'Координата {["X","Y","Z"][idx_v]}')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal', adjustable='datalim')

plot_projection(ax_xy, segments, P, 0, 1, 'Проекция XY')
plot_projection(ax_yz, segments, P, 1, 2, 'Проекция YZ')
plot_projection(ax_xz, segments, P, 0, 2, 'Проекция XZ')

handles, labels = ax_xy.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=4, fontsize=9)
plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('result.svg', dpi=150)
plt.show()