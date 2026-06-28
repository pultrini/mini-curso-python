# Aula 4 — Funções

## O que é uma função?

Uma função é um **bloco de código reutilizável** que executa uma tarefa específica. Pense nela como uma receita: você define uma vez e quantas vezes quiser.

```python
def saudacao():
    print("Olá, bem-vindo à monitoria de Python!")

saudacao()  # chamada da função
saudacao()  # pode chamar quantas vezes quiser
```

## Parâmetros e argumentos

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Maria")    # Olá, Maria!
saudacao("João")     # Olá, João!
```

> **Parâmetro** é o nome na definição. **Argumento** é o valor passado na chamada.

### Múltiplos parâmetros

```python
def calcular_area_retangulo(base, altura):
    area = base * altura
    print(f"Área: {area}")

calcular_area_retangulo(5, 3)  # Área: 15
```

## `return` — Retornando valores

```python
def somar(a, b):
    return a + b

resultado = somar(10, 5)
print(resultado)  # 15
```

> `print()` mostra na tela. `return` devolve o valor para quem chamou.

```python
# Sem return, a função retorna None implicitamente
def imprimir_soma(a, b):
    print(a + b)

valor = imprimir_soma(3, 4)  # imprime 7
print(valor)                  # None
```

## Argumentos nomeados

```python
def descricao_paciente(nome, idade, peso):
    print(f"{nome}, {idade} anos, {peso} kg")

# Por posição
descricao_paciente("Ana", 25, 60.5)

# Por nome (a ordem não importa)
descricao_paciente(peso=60.5, nome="Ana", idade=25)
```

## Valores padrão

```python
def calcular_imc(peso, altura=1.70):
    return peso / (altura ** 2)

print(calcular_imc(70))         # usa altura padrão 1.70
print(calcular_imc(70, 1.80))   # usa 1.80
```

> Parâmetros com valor padrão devem vir **depois** dos sem padrão.

```python
# ERRO:
def func(x=1, y):   # SyntaxError!
    pass

# CORRETO:
def func(y, x=1):
    pass
```

## Escopo local vs global

```python
x = 10  # variável global

def minha_funcao():
    x = 20  # variável LOCAL (só existe dentro da função)
    print(f"Dentro: {x}")

minha_funcao()       # Dentro: 20
print(f"Fora: {x}")  # Fora: 10
```

> Variáveis criadas dentro de uma função são **locais** — não existem fora dela.

```python
# Para modificar uma variável global (use com cuidado!)
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
print(contador)  # 2
```

> **Dica:** Evite `global` sempre que possível. Prefira passar valores por parâmetro e retorno.

## Docstrings — Documentando funções

```python
def calcular_dose(equivalente, massa):
    """Calcula a dose absorvida em Gray (Gy).

    Parâmetros:
        equivalente (float): equivalente de dose em Sievert (Sv)
        massa (float): massa em quilogramas (kg)

    Retorna:
        float: dose absorvida em Gray (Gy)
    """
    return equivalente / massa
```

```python
help(calcular_dose)  # mostra a docstring
```

## Funções com múltiplos retornos

```python
def estatisticas(numeros):
    media = sum(numeros) / len(numeros)
    menor = min(numeros)
    maior = max(numeros)
    return media, menor, maior

m, men, mai = estatisticas([4, 8, 2, 10, 6])
print(f"Média: {m}, Menor: {men}, Maior: {mai}")
```

> Na verdade, retorna uma **tupla** `(media, menor, maior)`.

## Recursão

Uma função que **chama a si mesma**. Útil para problemas que se dividem em subproblemas.

### Fatorial

```python
def fatorial(n):
    if n <= 1:
        return 1          # caso base
    return n * fatorial(n - 1)  # caso recursivo

print(fatorial(5))  # 120  (5 × 4 × 3 × 2 × 1)
```

### Fibonacci

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
# 0 1 1 2 3 5 8 13 21 34
```

> **Atenção:** Sempre defina um **caso base** (condição de parada). Sem ele, a recursão é infinita e estoura a pilha (`RecursionError`).

## Funções como argumentos

```python
def aplicar(func, valor):
    return func(valor)

def dobrar(x):
    return x * 2

print(aplicar(dobrar, 5))  # 10
```

## Resumo

```python
# Definição
def nome_funcao(parametros):
    """Docstring."""
    # corpo
    return resultado

# Chamada
resultado = nome_funcao(argumentos)

# Características:
# - Parâmetros com valor padrão
# - Argumentos nomeados
# - Escopo local vs global
# - Recursão (caso base + caso recursivo)
```

---

**Exercício:** Veja o arquivo `exercicio_4.py` nesta mesma pasta para praticar.
