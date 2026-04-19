"""
Gera a figura do Problema X22B10T0 no padrão editorial do livro.
Saída: ../figuras/cap3/Tx22_fig.pdf
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

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
L     = 66e-4
alpha = 1.93e-7
k     = 0.81
q0    = 1e3
M     = 200

# ── Autovalores ───────────────────────────────────────────────────────────────
m_arr = np.arange(1, M + 1)
beta  = np.pi * m_arr
A     = alpha * beta**2 / L**2

# ── Discretização ─────────────────────────────────────────────────────────────
t_max = 300
t     = np.linspace(0, t_max, 600)

x_vals  = [0, L/4, L/2, 3*L/4, L]
x_names = ['$x = 0$', '$x = L/4$', '$x = L/2$', '$x = 3L/4$', '$x = L$']

# ── Solução ───────────────────────────────────────────────────────────────────
def temperatura(x, t_vec):
    cos_m      = np.cos(beta * x / L)
    exp_mat    = np.exp(-np.outer(A, t_vec))
    transiente = (2*L/np.pi**2) * (q0/k) * np.sum(
        (cos_m[:, None] / m_arr[:, None]**2) * exp_mat, axis=0
    )
    permanente = (alpha * q0 / k) * t_vec / L + (q0/k) * (-x + x**2/(2*L) + L/3)
    return permanente - transiente

# ── Paleta Okabe-Ito e traços distintos (padrão do livro) ─────────────────────
cores    = ['#D55E00', '#0072B2', '#009E73', '#CC79A7', '#E69F00']
tracados = ['-', '--', '-.', ':', (0, (5, 1))]

# ── Figura ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(6.69, 4.2))
fig.subplots_adjust(left=0.11, right=0.97, top=0.90, bottom=0.13)

for xi, label, cor, ls in zip(x_vals, x_names, cores, tracados):
    ax.plot(t, temperatura(xi, t), label=label, color=cor, linestyle=ls, linewidth=1.5)

ax.set_xlabel('Tempo (s)')
ax.set_ylabel(r'$T(x,\,t)$ ($^\circ$C)')
ax.set_title('Campo de temperatura transiente --- Problema X22B10T0')
ax.legend(loc='upper left')
ax.grid(True, linestyle='--', linewidth=0.4, alpha=0.6)
fig.savefig('../figuras/cap3/Tx22_fig.pdf', backend='pdf')
plt.show()
