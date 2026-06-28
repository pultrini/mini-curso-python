"""
Exercício 7 — NumPy
Complete os exercícios abaixo seguindo as instruções nos comentários.
"""

import numpy as np

# ============================================================
# Exercício 7.1: Criação de arrays
# Crie os seguintes arrays e imprima cada um:
#   a) Array de 0 a 9
#   b) Array de 10 a 50, de 5 em 5 (10, 15, 20, ..., 50)
#   c) Array de 5 zeros
#   d) Array de 3 uns
#   e) Array com 10 valores linearmente espaçados entre 0 e 1
# ============================================================

# TODO: crie os arrays usando np.arange, np.zeros, np.ones, np.linspace


# ============================================================
# Exercício 7.2: Operações vetorizadas
# Dados os arrays abaixo, calcule SEM usar loop:
#   a) Soma elemento a elemento
#   b) Produto elemento a elemento
#   c) Raiz quadrada de cada elemento de a
#   d) a elevado ao quadrado
# ============================================================

a = np.array([4, 9, 16, 25, 36])
b = np.array([1, 2, 3, 4, 5])

# TODO: calcule e imprima cada operação


# ============================================================
# Exercício 7.3: Estatísticas
# Dado o array de doses abaixo, calcule e imprima:
#   - Média
#   - Desvio padrão
#   - Valor mínimo
#   - Valor máximo
#   - Soma total
# ============================================================

doses = np.array([2.01, 1.98, 2.03, 2.00, 1.97, 2.02, 1.99, 2.01, 2.00, 1.98])

# TODO: use np.mean, np.std, np.min, np.max, np.sum


# ============================================================
# Exercício 7.4: Indexação e slicing
# Dado o array abaixo, imprima:
#   a) O primeiro elemento
#   b) O último elemento
#   c) Os elementos do índice 2 ao 5 (inclusive)
#   d) Todos os elementos pares (dica: arr[arr % 2 == 0])
# ============================================================

arr = np.array([10, 23, 45, 67, 88, 12, 34, 56, 78, 90])

# TODO: faça as indexações


# ============================================================
# Exercício 7.5: Matrizes
# Crie uma matriz 3x3 com os valores de 1 a 9 e:
#   a) Imprima a matriz
#   b) Imprima a shape
#   c) Imprima a segunda linha
#   d) Imprima a terceira coluna
#   e) Calcule a soma de todos os elementos
# ============================================================

# TODO: use np.array para criar a matriz


# ============================================================
# Exercício 7.6: Simulação de doses (física médica)
# Simule 100 medições de dose com distribuição normal:
#   doses = np.random.normal(media=2.0, desvio=0.1, size=100)
# Calcule e imprima:
#   - Média das doses
#   - Desvio padrão
#   - Quantas doses estão fora de 2.0 ± 0.2 Gy
#   - Percentual de doses dentro da faixa
# ============================================================

# TODO: gere as doses e faça as análises


# ============================================================
# Exercício 7.7: Operações com matrizes (imagem)
# Crie uma "imagem" 5x5 com valores aleatórios de 0 a 255:
#   img = np.random.randint(0, 256, (5, 5))
#   a) Normalize para 0-1 (divida por 255)
#   b) Aplique um limiar (threshold) de 0.5 → matriz booleana
#   c) Conte quantos pixels são "brancos" (acima do limiar)
# ============================================================

# TODO: crie a imagem e processe
