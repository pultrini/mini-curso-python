# Aula 7 — Bibliotecas Famosas (com foco em NumPy)

## O que é uma biblioteca?

Uma biblioteca é um **conjunto de código pronto** que você importa e usa. Em vez de reinventar a roda, você importa a roda.

```python
import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.141592653589793
print(math.log(100, 10)) # 2.0
```

## Formas de importar

```python
import math                    # importa tudo, uso: math.sqrt()
from math import sqrt          # importa só sqrt, uso: sqrt()
from math import sqrt, pi      # importa várias
import math as m               # apelido, uso: m.sqrt()
from math import *             # importa tudo direto (EVITE — polui o namespace)
```

## Instalando bibliotecas com `pip`

```bash
pip install numpy
pip install matplotlib
pip install pandas
```

> Em alguns sistemas, use `pip3` em vez de `pip`.

---

## NumPy — Computação numérica

NumPy é a biblioteca fundamental para computação científica em Python. Ela fornece arrays multidimensionais muito mais rápidos que listas do Python.

### Por que NumPy?

```python
# Com lista Python: lento
lista = list(range(1_000_000))
soma = sum([x ** 2 for x in lista])

# Com NumPy: rápido (operação vetorizada)
import numpy as np
arr = np.arange(1_000_000)
soma = np.sum(arr ** 2)
```

> NumPy executa operações em C internamente — até 100x mais rápido.

### Criando arrays

```python
import numpy as np

# A partir de lista
arr = np.array([1, 2, 3, 4, 5])
print(arr)         # [1 2 3 4 5]
print(arr.dtype)   # int64

# Arrays especiais
np.zeros(5)         # [0. 0. 0. 0. 0.]
np.ones(3)          # [1. 1. 1.]
np.arange(0, 10, 2) # [0 2 4 6 8]
np.linspace(0, 1, 5) # [0.   0.25 0.5  0.75 1.  ]

# Matriz 2D
matriz = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matriz.shape)  # (2, 3) — 2 linhas, 3 colunas
```

### Operações vetorizadas

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)      # [11 22 33 44]
print(a * b)      # [10 40 90 160]
print(a ** 2)     # [1 4 9 16]
print(np.sqrt(a)) # [1.   1.41 1.73 2.  ]
print(np.exp(a))  # [ 2.72  7.39 20.09 54.60]
```

> **Sem loops!** O NumPy aplica a operação elemento a elemento automaticamente.

### Indexação e slicing

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])      # 10
print(arr[-1])     # 50
print(arr[1:4])    # [20 30 40]
print(arr[::2])    # [10 30 50]

# Matriz 2D
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(mat[0, 0])   # 1
print(mat[1, :])   # [4 5 6]  (linha inteira)
print(mat[:, 2])   # [3 6 9]  (coluna inteira)
print(mat[0:2, 1:3])  # [[2 3] [5 6]]
```

### Funções úteis

```python
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

print(np.sum(arr))    # 31
print(np.mean(arr))   # 3.875
print(np.std(arr))    # 2.47
print(np.min(arr))    # 1
print(np.max(arr))    # 9
print(np.sort(arr))   # [1 1 2 3 4 5 6 9]
print(np.argmax(arr)) # 5 (índice do maior)
```

### `reshape`

```python
arr = np.arange(12)
mat = arr.reshape(3, 4)
print(mat)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
```

### Exemplo: vetor de doses em radioterapia

```python
import numpy as np

doses = np.array([2.0, 2.1, 1.9, 2.05, 2.02, 1.98, 2.03])

print(f"Dose média: {np.mean(doses):.3f} Gy")
print(f"Desvio padrão: {np.std(doses):.3f} Gy")
print(f"Dose máxima: {np.max(doses):.3f} Gy")
print(f"Dose mínima: {np.min(doses):.3f} Gy")
print(f"Variação: {np.max(doses) - np.min(doses):.3f} Gy")
```

### Exemplo: imagem como matriz

```python
import numpy as np

# Simular uma imagem 5x5 (valores de intensidade)
imagem = np.random.randint(0, 256, (5, 5))
print("Imagem:")
print(imagem)

# Normalizar para 0-1
imagem_norm = imagem / 255.0
print("\nNormalizada:")
print(imagem_norm)

# Limiarização (threshold)
limiar = 0.5
binaria = imagem_norm > limiar
print("\nBinária (limiar 0.5):")
print(binaria)
```

---

## Outras bibliotecas importantes (menção)

### Matplotlib — Gráficos

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Função Seno")
plt.xlabel("x")
plt.ylabel("sen(x)")
plt.grid(True)
plt.show()
```

### Pandas — Dados tabulares

```python
import pandas as pd

dados = {
    "paciente": ["Ana", "João", "Maria"],
    "dose_Gy": [2.0, 1.8, 2.1],
    "frações": [30, 25, 30]
}

df = pd.DataFrame(dados)
print(df)
print(f"\nDose média: {df['dose_Gy'].mean():.2f} Gy")
```

### SciPy — Científico

```python
from scipy import constants

print(constants.c)         # velocidade da luz
print(constants.h)         # constante de Planck
print(constants.physical_constants['proton mass'])
```

---

## Resumo

```python
# Importar
import numpy as np
from math import sqrt

# NumPy — criar arrays
np.array([1, 2, 3])
np.zeros(5)
np.arange(0, 10, 2)
np.linspace(0, 1, 5)

# Operações vetorizadas (sem loop!)
a + b, a * b, np.sqrt(a)

# Funções agregadas
np.sum(), np.mean(), np.std(), np.max(), np.min()

# Reshape
arr.reshape(linhas, colunas)
```

---

**Exercício:** Veja o arquivo `exercicio_7.py` nesta mesma pasta para praticar.
