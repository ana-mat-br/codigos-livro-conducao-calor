"""
Gera a figura do Problema X23B10T0 no padrão editorial do livro.
Parâmetros: L=66e-4 m, alpha=1.93e-7 m²/s, k=0.81 W/(m·K),
            q0=1e3 W/m², h2=25 W/(m²·K), H2=h2*L/k ≈ 0.204
Saída: ../figuras/cap4/Tx23_fig.pdf
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import brentq

# ── Estilo tipográfico (padrão do livro) ──────────────────────────────────────
mpl.rcParams.update({
    'text.usetex'        : True,
    'font.family'        : 'serif',
    'font.serif'         : ['Palatino'],
    'text.latex.preamble': r'\usepackage{mathpazo}\usepackage{amsmath}',
    'axes.labelsize'     : 11,
    'xtick.labelsize'    : 10,
    'ytick.labelsize'    : 10,
    'legend.fontsize'    : 9,
    'axes.titlesize'     : 11,
})

# ── Parâmetros físicos ────────────────────────────────────────────────────────
L     = 66e-4        # m
alpha = 1.93e-7      # m²/s
k     = 0.81         # W/(m·K)
q0    = 1e3          # W/m²
h2    = 25.0         # W/(m²·K)
H2    = h2 * L / k  # adimensional ≈ 0.204
M     = 300          # termos da série

# ── Autovalores: β_m tan(β_m) = H2 ───────────────────────────────────────────
eps = 1e-10
b_m = np.array([
    brentq(lambda b: b * np.tan(b) - H2,
           (m - 1) * np.pi + eps,
           (m - 1) * np.pi + np.pi / 2 - eps)
    for m in range(1, M + 1)
])
A_m  = alpha * b_m**2 / L**2
Cm   = 2 * (b_m**2 + H2**2) / (L * (b_m**2 + H2**2 + H2))

# ── Discretização ─────────────────────────────────────────────────────────────
t_max = 100
t     = np.linspace(0.01, t_max, 800)

x_vals  = [0, L/4, L/2, 3*L/4, L]
x_names = [r'$x = 0$', r'$x = L/4$', r'$x = L/2$', r'$x = 3L/4$', r'$x = L$']

# ── Solução ───────────────────────────────────────────────────────────────────
def temperatura(x):
    cos_m  = np.cos(b_m * x / L)
    trans  = (alpha * q0 / k) * np.einsum(
        'm,mt->t', Cm * cos_m / A_m, np.exp(-np.outer(A_m, t)))
    perm   = q0 * (L - x) / k + q0 / h2
    return perm - trans

# ── Verificação da CI ─────────────────────────────────────────────────────────
for x_chk in [0.0, L / 2, L]:
    print(f'T(x={x_chk/L:.2f}L, t≈0) = {temperatura(x_chk)[0]:.4f} °C  (esperado ≈ 0)')

# ── Paleta Okabe-Ito e traços distintos (padrão do livro) ─────────────────────
cores    = ['#D55E00', '#0072B2', '#009E73', '#CC79A7', '#E69F00']
tracados = ['-', '--', '-.', ':', (0, (5, 1))]

# ── Figura ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6.69, 4.2))
fig.subplots_adjust(left=0.11, right=0.97, top=0.90, bottom=0.13)

for x, label, cor, ls in zip(x_vals, x_names, cores, tracados):
    ax.plot(t, temperatura(x), label=label, color=cor, linestyle=ls, linewidth=1.5)

ax.set_xlabel('Tempo (s)')
ax.set_ylabel(r'$T(x,\,t)$ ($^\circ$C)')
ax.set_title(r'Campo de temperatura transiente --- Problema X23B10T0 ($H_2 = {:.2f}$)'.format(H2))
ax.legend(loc='upper left')
ax.grid(True, linestyle='--', linewidth=0.4, alpha=0.6)

fig.savefig('../figuras/cap4/Tx23_fig.pdf', backend='pdf')
plt.show()
