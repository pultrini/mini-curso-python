# Aula 5 — Exercícios de Física Médica

## Por que Python em Física Médica?

Python é amplamente usado em pesquisa e indústria de física médica para:
- Simulações de decaimento radioativo
- Processamento de imagens médicas (TC, RMN)
- Cálculos de dosimetria e proteção radiológica
- Análise de dados experimentais

Nesta aula, aplicamos tudo o que aprendemos (variáveis, condicionais, loops, funções) em problemas reais da área.

---

## 1. Decaimento Radioativo

### Teoria

A atividade de um material radioativo decai exponencialmente:

$$N(t) = N_0 \cdot e^{-\lambda t}$$

Onde:
- $N_0$ = número inicial de átomos (ou atividade inicial)
- $\lambda$ = constante de decaimento (s⁻¹)
- $t$ = tempo (s)
- $N(t)$ = número de átomos no tempo $t$

A **atividade** $A$ é a taxa de decaimento:

$$A(t) = \lambda \cdot N(t) = A_0 \cdot e^{-\lambda t}$$

### Relação com meia-vida

$$t_{1/2} = \frac{\ln(2)}{\lambda} \approx \frac{0.693}{\lambda}$$

### Exemplo em Python

```python
import math

N0 = 1000          # átomos iniciais
lambda_dec = 0.1   # constante de decaimento (s⁻¹)
t = 5              # tempo em segundos

N = N0 * math.exp(-lambda_dec * t)
print(f"Átomos restantes após {t}s: {N:.1f}")
```

**Arquivo:** `decaimento_radioativo.py`

---

## 2. Lei de Beer-Lambert

### Teoria

Descreve como a luz é absorvida ao atravessar um meio:

$$I = I_0 \cdot e^{-\mu x}$$

Onde:
- $I_0$ = intensidade incidente
- $I$ = intensidade transmitida
- $\mu$ = coeficiente de atenuação linear (cm⁻¹)
- $x$ = espessura do material (cm)

A **transmitância** $T$ e **absorbância** $A$:

$$T = \frac{I}{I_0} = e^{-\mu x}$$

$$A = -\log_{10}(T) = \mu x \cdot \log_{10}(e)$$

### Aplicação

Usada em espectrofotometria, dosimetria de feixes e imagem médica.

**Arquivo:** `beer_lambert.py`

---

## 3. Dosimetria

### Teoria

**Dose absorvida** ($D$): energia depositada por unidade de massa.

$$D = \frac{dE}{dm} \quad \text{[Gray = J/kg]}$$

**Equivalente de dose** ($H$): dose absorvida ponderada pelo tipo de radiação.

$$H = D \cdot w_R \quad \text{[Sievert = Sv]}$$

**Fatores de ponderação** ($w_R$):

| Tipo de radiação | $w_R$ |
|---|---|
| Fótons (raios X, gama) | 1 |
| Elétrons, múons | 1 |
| Prótons | 2 |
| Nêutrons (energia dependente) | 5 - 20 |
| Alfa, fragmentos pesados | 20 |

**Dose efetiva** ($E$): ponderada pelos tecidos.

$$E = \sum_T w_T \cdot H_T$$

### Limites de dose (ICRP)

- Público: 1 mSv/ano (além da radiação natural)
- Trabalhador: 20 mSv/ano (média de 5 anos)

**Arquivo:** `dosimetria.py`

---

## 4. Tomografia Computadorizada (Backprojection)

### Teoria

A tomografia reconstrói imagens a partir de projeções em múltiplas ângulos.

O método mais simples é a **retroprojeção filtrada** (backprojection):

1. Coleta projeções em diferentes ângulos
2. "Espalha" cada projeção de volta pela imagem
3. Soma todas as contribuições

Para uma imagem $f(x,y)$ com projeções $p_\theta(t)$:

$$f(x,y) = \int_0^{\pi} p_\theta(x\cos\theta + y\sin\theta) \, d\theta$$

Na prática, discretizamos a integral como uma soma sobre ângulos.

**Arquivo:** `tomografia.py`

---

## 5. Meia-vida ($t_{1/2}$)

### Teoria

Tempo necessário para que a atividade caia à metade:

$$t_{1/2} = \frac{\ln(2)}{\lambda}$$

Isótopos comuns em medicina:

| Isótopo | $t_{1/2}$ | Uso |
|---|---|---|
| Tc-99m | 6.01 h | Cintilografia |
| I-131 | 8.02 d | Terapia de tireoide |
| F-18 | 109.8 min | PET |
| Co-60 | 5.27 a | Radioterapia |
| Cs-137 | 30.17 a | Braquiterapia |

**Arquivo:** `half_life.py`

---

## 6. Unidade Sievert e Conversões

### Teoria

O Sievert (Sv) é a unidade de equivalente de dose e dose efetiva no SI.

Conversões úteis:

| De | Para | Fator |
|---|---|---|
| 1 Sv | 1000 mSv | ×1000 |
| 1 mSv | 1000 μSv | ×1000 |
| 1 Gy (fótons) | 1 Sv | ×wR |
| 1 rem | 0.01 Sv | ×0.01 |

Fontes de exposição típicas (Brasil):

| Fonte | Dose anual média |
|---|---|
| Radiação natural (Rn, solo, cósmica) | ~2.4 mSv |
| Exames médicos | ~0.6 mSv |
| Alimentos (K-40, C-14) | ~0.3 mSv |
| Voo transatlântico | ~0.05 mSv/voo |

**Arquivo:** `unidade_sievert.py`

---

## Arquivos de exercícios

Cada arquivo `.py` nesta pasta é um **template** com comentários-guia. Complete o código seguindo as instruções.

| Arquivo | Tema |
|---|---|
| `decaimento_radioativo.py` | Lei exponencial N(t) |
| `beer_lambert.py` | Transmitância e absorbância |
| `dosimetria.py` | Dose absorvida e equivalente |
| `tomografia.py` | Backprojection simples |
| `half_life.py` | Cálculo de meia-vida |
| `unidade_sievert.py` | Conversões de unidades |
