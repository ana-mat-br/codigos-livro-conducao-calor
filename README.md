# Códigos do livro *Condução de Calor: Aplicações das Funções de Green em Problemas de Engenharia*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ana-mat-br/codigos-livro-conducao-calor)

**Autores:** Ana Paula Fernandes e Gilmar Guimarães

Este repositório reúne os *notebooks* interativos do livro, prontos para execução no Google Colab. Cada *notebook* implementa a solução analítica de um problema do texto e gera os gráficos correspondentes — basta clicar no badge "Abrir no Colab" para executar diretamente no navegador, sem necessidade de instalação.

## O que é o Google Colab?

O **Google Colab** (Colaboratory) é um ambiente gratuito mantido pela Google que executa código **Python** diretamente no navegador, sem qualquer instalação local — basta uma conta Google. Os arquivos `.ipynb` deste repositório são *notebooks Jupyter*: documentos interativos que combinam texto explicativo, fórmulas matemáticas, código e gráficos no mesmo lugar.

Em cada *notebook* você encontra:

- a **descrição do problema** (geometria, condições de contorno, condição inicial),
- a **solução analítica** apresentada no capítulo correspondente do livro,
- o **código Python** que avalia a solução com `numpy`/`matplotlib` e gera os gráficos,
- comentários didáticos ao longo do código, explicando cada passo.

## Como executar um *notebook*

1. Clique no badge ![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg) ao lado do *notebook* desejado, na lista abaixo.
2. Faça login com sua conta Google, caso ainda não esteja logado.
3. No menu superior, escolha **Ambiente de execução → Executar tudo** para rodar todas as células de uma vez; ou pressione **Shift+Enter** dentro de uma célula para executá-la individualmente.

> 💡 **Dica:** edite à vontade os parâmetros físicos (`L`, `alpha`, `k`, `q0`, ...) e re-execute para ver como a solução responde. Para guardar uma versão sua, use **Arquivo → Salvar uma cópia no Drive** — isso não altera o *notebook* original deste repositório.

---

## Capítulo 2 — O Método das Funções de Green: Formulação e Interpretação

### 🌡️ [`x21b11t1.ipynb`](https://colab.research.google.com/github/ana-mat-br/codigos-livro-conducao-calor/blob/main/x21b11t1.ipynb) — Problema X21B11T1

Placa plana de espessura $L$ com:

- $x = 0$ (tipo 2): fluxo de calor prescrito $q''_0$
- $x = L$ (tipo 1): temperatura prescrita $T_1$
- Condição inicial: $T(x,0) = T_0$

Caso geral em que ambas as condições de contorno são não nulas (B11) e a temperatura inicial difere da temperatura prescrita ($T_0 \neq T_1$). O *notebook* mostra a decomposição da solução em três termos: regime permanente, transiente do fluxo e transiente da condição inicial.

### 📐 [`x21_formas_fechadas.ipynb`](https://colab.research.google.com/github/ana-mat-br/codigos-livro-conducao-calor/blob/main/x21_formas_fechadas.ipynb) — Forma fechada para o Problema X21

Demonstração computacional da vantagem da forma fechada no Problema X21B10T0. Compara a Eq. (2.51), com dois somatórios (série estacionária de convergência lenta), à Eq. (2.52), que usa a forma fechada $\sum \cos(\beta_m x/L)/\beta_m^2 = (1/2)(1 - x/L)$ e converge com pouquíssimos termos.

---

## Capítulo 3 — Fluxo de Calor Imposto: Placa Finita e Meio Semi-infinito

### 📐 [`x22_formas_fechadas.ipynb`](https://colab.research.google.com/github/ana-mat-br/codigos-livro-conducao-calor/blob/main/x22_formas_fechadas.ipynb) — Forma fechada para o Problema X22

Demonstração computacional da forma fechada no Problema X22B10T0 (placa com superfície isolada em $x=L$). Compara a série estacionária $(2L/\pi^2)\sum \cos(m\pi x/L)/m^2$, de convergência lenta, à forma fechada $-x + x^2/(2L) + L/3$, que dá o resultado exato com $M=1$ termo.

### 🌡️ [`x22b10t0.ipynb`](https://colab.research.google.com/github/ana-mat-br/codigos-livro-conducao-calor/blob/main/x22b10t0.ipynb) — Problema X22B10T0

Placa plana de espessura $L$ com:

- $x = 0$ (tipo 2): fluxo de calor prescrito $q''_0$
- $x = L$ (tipo 2): superfície isolada (fluxo nulo)
- Condição inicial: $T(x,0) = 0$

Solução em série de Fourier (Eq. 3.19) com $\beta_m = m\pi$. Plota a evolução temporal de $T(x,t)$ em cinco posições.

### 🌡️ [`x20b10t0.ipynb`](https://colab.research.google.com/github/ana-mat-br/codigos-livro-conducao-calor/blob/main/x20b10t0.ipynb) — Problema X20B1T0

Meio semi-infinito com:

- $x = 0$ (tipo 2): fluxo de calor prescrito $q''_0$
- $x \to \infty$: temperatura não perturbada
- Condição inicial: $T(x,0) = 0$

Solução em forma fechada usando a integral da função erro complementar:
$\Theta(x,t) = (q''_0/k)(4\alpha t)^{1/2}\,\mathrm{ierfc}\bigl(x/(4\alpha t)^{1/2}\bigr)$.

---

## Capítulo 4 — Condição de Contorno Convectiva: Placa Finita com Fluxo Imposto

### 🌡️ [`x23b10t0.ipynb`](https://colab.research.google.com/github/ana-mat-br/codigos-livro-conducao-calor/blob/main/x23b10t0.ipynb) — Problema X23B10T0

Placa plana de espessura $L$ com:

- $x = 0$ (tipo 2): fluxo de calor prescrito $q''_0$
- $x = L$ (tipo 3): convecção com coeficiente $h_2$ e $T_\infty = 0$
- Condição inicial: $T(x,0) = 0$

Solução via funções de Green com autovalores obtidos pelo método de Brent (raízes de $\xi\tan\xi = H_2$).

### 🔢 [`gx13_autovalores.ipynb`](https://colab.research.google.com/github/ana-mat-br/codigos-livro-conducao-calor/blob/main/gx13_autovalores.ipynb) — Autovalores GX13: Brent vs Beck (1992)

Problema GX13: temperatura prescrita em $x=0$ (tipo 1) e convecção em $x=L$ (tipo 3). Compara os autovalores obtidos pelo método de **Brent** para a equação $\xi\cot\xi = -H_2$ com as fórmulas aproximadas de Beck (1992) — Eqs. (4.22)–(4.25) — e com a correção iterativa de Newton-Raphson (Eq. 4.26). Tabela de erros relativos para diferentes valores de $H_2$.

### 🔢 [`gx23_autovalores.ipynb`](https://colab.research.google.com/github/ana-mat-br/codigos-livro-conducao-calor/blob/main/gx23_autovalores.ipynb) — Autovalores GX23: Brent vs Beck (1992)

Problema GX23: fluxo prescrito em $x=0$ (tipo 2) e convecção em $x=L$ (tipo 3). Compara os autovalores obtidos pelo método de **Brent** para a equação $\xi\tan\xi = H_2$ com as fórmulas aproximadas de Beck (1992) — Eqs. (4.29)–(4.31) — e com a correção iterativa de Newton-Raphson (Eq. 4.33). Tabela de erros relativos para diferentes valores de $H_2$.

---

## Convenção de notação

A notação **XIJBKLTM** identifica geometria e condições de contorno do problema:

| Posição | Significado |
|---|---|
| **X** | Geometria plana (cartesiana 1D) |
| **I** | Tipo de condição em $x = 0$: 0 = semi-infinito, 1 = temperatura, 2 = fluxo, 3 = convecção |
| **J** | Tipo de condição em $x = L$: 0 = ausente, 1 = temperatura, 2 = fluxo (incluindo isolada), 3 = convecção |
| **BKL** | Indica se as condições de contorno são não-homogêneas (1) ou nulas (0) |
| **TM** | Indica se a condição inicial é não-nula (1) ou nula (0) |

O prefixo **G** designa problemas formulados em termos da função de Green correspondente.

---

## Uso de assistência de IA

A elaboração dos códigos deste repositório e a revisão de redação dos textos do livro contaram com o auxílio de ferramentas de inteligência artificial generativa. As ferramentas foram empregadas como apoio à geração, depuração e documentação de implementações em Python e à revisão linguística do material. **A concepção, a validação técnica e a responsabilidade autoral pelo conteúdo final são integralmente dos autores, Ana Paula Fernandes e Gilmar Guimarães.**
