"""
Problema X21B10T0 — Condução de calor transiente 1D
Solução via Funções de Green (Eq. 2.52 do livro)

Placa plana (0 <= x <= L):
  - Fluxo prescrito em x = 0:  -k dT/dx|_{x=0} = q0
  - Temperatura prescrita em x = L:  T(L,t) = T1
  - Condição inicial:  T(x,0) = T1

Solução (forma fechada):
  T(x,t) = T1 + Theta(x,t)

  Theta(x,t) = (q0/k)(L - x)
               - (2*alpha/L)*(q0/k) * sum_{m=1}^{M} [e^{-A_m*t} * cos(beta_m*x/L) / A_m]

  beta_m = pi*(m - 1/2),   m = 1, 2, 3, ...
  A_m    = alpha * beta_m^2 / L^2
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# ── Estilo tipográfico (fontes iguais ao livro) ───────────────────────────────
mpl.rcParams.update({
    'text.usetex'        : True,
    'font.family'        : 'serif',
    'font.serif'         : ['Palatino'],
    'text.latex.preamble': r'\usepackage{mathpazo}',
    'axes.labelsize'     : 11,
    'xtick.labelsize'    : 10,
    'ytick.labelsize'    : 10,
    'axes.titlesize'     : 11,
})

# ── Parâmetros físicos e geométricos ──────────────────────────────────────────
L     = 66e-4        # espessura da placa [m]
alpha = 1.93e-7      # difusividade térmica [m²/s]
k     = 0.81         # condutividade térmica [W/(m·K)]
q0    = 1e3          # fluxo de calor em x=0 [W/m²]
T1    = 40.0         # temperatura inicial e em x=L [°C]

M     = 200          # número de termos da série

# ── Autovalores e coeficientes ────────────────────────────────────────────────
m_arr = np.arange(1, M + 1)
beta  = np.pi * (m_arr - 0.5)
A     = alpha * beta**2 / L**2

# ── Malhas de tempo e posição ─────────────────────────────────────────────────
t_max = 500
t     = np.linspace(0, t_max, 600)

x_vals  = [0, L/4, L/2, 3*L/4, L]
x_names = [r'$x = 0$', r'$x = L/4$', r'$x = L/2$', r'$x = 3L/4$', r'$x = L$']

# Paleta Okabe-Ito (acessível para daltônicos) + traços distintos para P&B
estilos = [
    dict(color='#000000', linestyle='-',          linewidth=1.5),  # preto   sólido
    dict(color='#0072B2', linestyle='--',         linewidth=1.5),  # azul    tracejado
    dict(color='#D55E00', linestyle='-.',         linewidth=1.5),  # laranja traço-ponto
    dict(color='#009E73', linestyle=':',          linewidth=2.0),  # verde   pontilhado
    dict(color='#CC79A7', linestyle=(0, (5, 1)),  linewidth=1.5),  # roxo    tracejado fino
]

# ── Cálculo da solução ────────────────────────────────────────────────────────
def temperatura(x, t_vec):
    cos_m      = np.cos(beta * x / L)
    exp_mat    = np.exp(-np.outer(A, t_vec))
    transiente = (2 * alpha / L) * (q0 / k) * np.sum(
        (cos_m[:, None] * exp_mat) / A[:, None], axis=0
    )
    return T1 + (q0 / k) * (L - x) - transiente

# ── Gráfico ───────────────────────────────────────────────────────────────────
# largura = largura do texto do livro (17 cm = 6.69 pol)
# margem direita alargada para os rótulos das curvas
fig, ax = plt.subplots(figsize=(6.69, 4.0))
fig.subplots_adjust(left=0.10, right=0.80, top=0.92, bottom=0.13)

for xi, label, estilo in zip(x_vals, x_names, estilos):
    T_curve = temperatura(xi, t)
    ax.plot(t, T_curve, **estilo)
    # rótulo direto no final de cada curva (fora da área do gráfico)
    ax.annotate(
        label,
        xy=(1.0, T_curve[-1]),
        xycoords=('axes fraction', 'data'),
        xytext=(6, 0),
        textcoords='offset points',
        va='center',
        fontsize=10,
        color=estilo['color'],
        clip_on=False,
    )

ax.set_xlabel('Tempo (s)')
ax.set_ylabel(r'Temperatura ($^\circ$C)')
ax.set_title(r'Campo de temperatura transiente --- Problema X21B10T0')
ax.grid(True, linestyle='--', linewidth=0.4, alpha=0.6)
ax.set_xlim(0, t_max)

# salva como PDF (vetorial) e PNG de alta resolução
fig.savefig('../figuras/cap2/Tx21_fig.pdf', backend='pdf')
fig.savefig('../figuras/cap2/Tx21_fig.png', dpi=300)
plt.show()
print("Figuras salvas em figuras/cap2/Tx21_fig.pdf e .png")
