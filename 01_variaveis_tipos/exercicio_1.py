"""
Exercício 1 — Variáveis e Tipos
Complete os exercícios abaixo seguindo as instruções nos comentários.
"""

# ============================================================
# Exercício 1.1: Declaração de variáveis
# Crie as seguintes variáveis com os valores indicados:
# - nome (seu nome completo)
# - idade (sua idade em anos)
# - altura (sua altura em metros, como float)
# - estudante (True ou False)
# ============================================================

# TODO: declare as variáveis aqui
nome = "Davi Rodrigues Pultrini"
idade = 20
altura = 1.75
estudante = True

# ============================================================
# Exercício 1.2: Tipos de dados
# Use type() para imprimir o tipo de cada variável criada acima
# ============================================================

# TODO: imprima os tipos
print(type(nome))      # str
print(type(idade))     # int
print(type(altura))    # float
print(type(estudante)) # bool

# ============================================================
# Exercício 1.3: Conversão de tipos
# Dado o valor abaixo, converta para os tipos indicados e imprima
# ============================================================

valor_str = "3.14"

# TODO: converta para float
valor_float = float(valor_str)  # substitua None

# TODO: converta para int (cuidado: int() de float trunca!)
valor_int = int(valor_float)  # substitua None

# TODO: verifique o tipo de cada conversão
type(valor_float), type(valor_int)


# ============================================================
# Exercício 1.4: f-strings
# Imprima uma frase usando f-string com suas variáveis
# Exemplo: "Meu nome é Ana, tenho 20 anos e 1.65m de altura."
# ============================================================

# TODO: use f-string para imprimir uma frase com nome, idade e altura

print(f"meu nome é {nome}, tenho {idade} anos e {altura}m de altura.")


# ============================================================
# Exercício 1.5: Operadores aritméticos
# Dados dois números, calcule e imprima:
# - Soma
# - Subtração
# - Multiplicação
# - Divisão (float)
# - Divisão inteira
# - Resto da divisão
# - Potência (a elevado a b)
# ============================================================

a = 17
b = 5

# TODO: calcule e imprima cada operação

print(f"Soma: {a + b}")
print(f"Subtração: {a - b}")
print(f"Multiplicação: {a * b}")
print(f"Divisão (float): {a / b}")
print(f"Divisão inteira: {a // b}")
print(f"Resto da divisão: {a % b}")
print(f"Potência: {a ** b}")


# ============================================================
# Exercício 1.6: Área e perímetro
# Peça ao usuário a largura e altura de um retângulo (use input())
# Calcule e imprima a área e o perímetro
# ============================================================

# TODO: use input() para obter largura e altura
# Dica: converta o input para float!
# largura = float(input("Largura: "))
# Calcule area = largura * altura
# Calcule perimetro = 2 * (largura + altura)

largura = float(input("Largura: "))
altura = float(input("Altura: "))
area = largura * altura
perimetro = 2 * (largura + altura)

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")


# ============================================================
# Exercício 1.7: Conversão de temperatura
# Converta uma temperatura de Celsius para Fahrenheit
# Fórmula: F = C × 9/5 + 32
# Peça ao usuário a temperatura em Celsius
# ============================================================

# TODO: peça a temperatura e converta
celsius = float(input("Temperatura em Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"Temperatura em Fahrenheit: {fahrenheit}")