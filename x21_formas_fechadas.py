"""
Formas Fechadas para o Problema X21 — demonstração computacional
Seção 2.9 do livro

Dois painéis:
  Esquerdo — convergência do somatório estacionário da Eq. (2.51)
             para M = 1, 2, 5, 20 termos vs. forma fechada exata
  Direito  — T(x=0, t) calculada pela Eq. (2.51) com poucos termos
             vs. Eq. (2.52) com M=1 (usando forma fechada)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# ── Estilo tipográfico ────────────────────────────────────────────────────────
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
T1    = 40.0

M_max = 500
m_arr = np.arange(1, M_max + 1)
beta  = np.pi * (m_arr - 0.5)
A     = alpha * beta**2 / L**2

# ── Paleta Okabe-Ito ──────────────────────────────────────────────────────────
cores     = ['#D55E00', '#0072B2', '#009E73', '#CC79A7']
tracados  = ['--', '-.', ':', (0, (5, 1))]
espessuras = [1.4, 1.4, 1.8, 1.4]

# ── Painel esquerdo: convergência do somatório estacionário ───────────────────
# Compara sum cos(beta_m x/L)/beta_m^2 vs forma fechada (1/2)(1 - x/L)
x_norm = np.linspace(0, 1, 400)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.69*1.3, 4.2))
fig.subplots_adjust(left=0.09, right=0.97, top=0.90, bottom=0.13, wspace=0.32)

M_vals = [1, 2, 5, 20]
for M_val, cor, ls, lw in zip(M_vals, cores, tracados, espessuras):
    serie = np.sum(
        np.cos(np.outer(beta[:M_val], x_norm)) / beta[:M_val, None]**2,
        axis=0
    )
    ax1.plot(x_norm, serie, color=cor, linestyle=ls, linewidth=lw,
             label=f'$M = {M_val}$')

forma_fechada = 0.5 * (1 - x_norm)
ax1.plot(x_norm, forma_fechada, color='black', linestyle='-', linewidth=1.5,
         label=r'Forma fechada')

ax1.set_xlabel('$x/L$')
ax1.set_ylabel(r'$\displaystyle\sum_{m=1}^{M}\dfrac{\cos(\beta_m x/L)}{\beta_m^2}$',
               labelpad=4)
ax1.set_title(r'Convergência da série estacionária')
ax1.legend(loc='upper right')
ax1.grid(True, linestyle='--', linewidth=0.4, alpha=0.6)
ax1.set_xlim(0, 1)

# ── Painel direito: T(x=0, t) — série vs. forma fechada ──────────────────────
t = np.linspace(0, 500, 600)
x = 0.0

def T_serie(M_val, t_vec):
    """Eq. (2.51): dois somatórios, sem forma fechada."""
    bm  = beta[:M_val]
    Am  = A[:M_val]
    cm  = np.cos(bm * x / L)
    ss  = (2*alpha/L) * (q0/k) * np.sum(cm / Am)
    tr  = (2*alpha/L) * (q0/k) * np.sum(
        (cm[:, None] * np.exp(-np.outer(Am, t_vec))) / Am[:, None], axis=0
    )
    return T1 + ss - tr

def T_fechada(M_val, t_vec):
    """Eq. (2.52): forma fechada + somatório transiente."""
    bm  = beta[:M_val]
    Am  = A[:M_val]
    cm  = np.cos(bm * x / L)
    perm = (q0/k) * (L - x)
    tr   = (2*alpha/L) * (q0/k) * np.sum(
        (cm[:, None] * np.exp(-np.outer(Am, t_vec))) / Am[:, None], axis=0
    )
    return T1 + perm - tr

# referência com muitos termos
T_ref = T_fechada(200, t)
ax2.plot(t, T_ref, color='black', linestyle='-', linewidth=1.5,
         label=r'Referência ($M=200$)')

# Eq. (2.51) com M = 1, 2, 5
for M_val, cor, ls, lw in zip([1, 2, 5], cores[:3], tracados[:3], espessuras[:3]):
    ax2.plot(t, T_serie(M_val, t), color=cor, linestyle=ls, linewidth=lw,
             label=fr'Eq.\,(2.51), $M={M_val}$')

# Eq. (2.52) com M = 1
ax2.plot(t, T_fechada(1, t), color=cores[3], linestyle=tracados[3],
         linewidth=espessuras[3], label=r'Eq.\,(2.52), $M=1$')

ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel(r'$T(0,\,t)$ ($^\circ$C)')
ax2.set_title(r'$T(x=0,\,t)$: convergência em número de termos')
ax2.legend(loc='center right')
ax2.grid(True, linestyle='--', linewidth=0.4, alpha=0.6)
ax2.set_xlim(0, 500)

fig.savefig('../figuras/cap2/formas_fechadas.pdf', backend='pdf')
fig.savefig('../figuras/cap2/formas_fechadas.png', dpi=300)
plt.show()
print("Figuras salvas em figuras/cap2/formas_fechadas.pdf e .png")
