"""
Exercício 2 — Fluxo de Código
Complete os exercícios abaixo seguindo as instruções nos comentários.
"""

# ============================================================
# Exercício 2.1: Par ou ímpar
# Peça um número ao usuário e imprima se é par ou ímpar
# ============================================================

# TODO: use input() e o operador %
valor = int(input("Digite um número: "))
if valor % 2 == 0:
    print(f"{valor} é par.")
else:
    print(f"{valor} é ímpar.")



# ============================================================
# Exercício 2.2: Classificação de nota
# Dada uma nota de 0 a 10, classifique:
#   A: 9 a 10
#   B: 7 a 8.9
#   C: 5 a 6.9
#   D: abaixo de 5
# ============================================================

nota = 7.5

# TODO: use if/elif/else para classificar e imprimir

if nota >= 9:
    print("Classificação: A")
elif nota >= 7:
    print("Classificação: B")
elif nota >= 5:
    print("Classificação: C")
else:
    print("Classificação: D")



# ============================================================
# Exercício 2.3: Verificação de idade
# Peça a idade do usuário e imprima:
#   - "Criança" se menor de 12
#   - "Adolescente" se entre 12 e 17
#   - "Adulto" se entre 18 e 64
#   - "Idoso" se 65 ou mais
# ============================================================

# TODO: use input() e if/elif/else

idade = int(input("Digite sua idade: "))
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")


# ============================================================
# Exercício 2.4: Operadores lógicos
# Dados dois valores booleanos, imprima a tabela-verdade
# para AND, OR e NOT
# ============================================================

a = True
b = False

# TODO: imprima a, b, a and b, a or b, not a, not b
print("a:", a)
print("b:", b)
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
print("not b:", not b)


# ============================================================
# Exercício 2.5: Verificação de faixa
# Verifique se um número está entre 10 e 20 (inclusive)
# Use o operador 'and' e depois tente com encadeamento (10 <= x <= 20)
# ============================================================

numero = 15

# TODO: verifique e imprima se está na faixa
if 10 <= numero <= 20:
    print(f"{numero} está entre 10 e 20.")
else:
    print(f"{numero} não está entre 10 e 20.")


# ============================================================
# Exercício 2.6: Calculadora simples
# Peça dois números e uma operação (+, -, *, /)
# Imprima o resultado. Se a operação for inválida, avise.
# Se for divisão por zero, avise.
# ============================================================

# TODO: use input() e if/elif/else

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"Resultado: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"Resultado: {resultado}")
elif operacao == "/":
    if numero2 == 0:
        print("Erro: Divisão por zero.")
    else:
        resultado = numero1 / numero2
        print(f"Resultado: {resultado}")
else:
    print("Erro: Operação inválida.")



# ============================================================
# Exercício 2.7: Ano bissexto
# Um ano é bissexto se:
#   - É divisível por 4 E
#   - NÃO é divisível por 100, EXCETO se for divisível por 400
# Exemplos: 2000 (bissexto), 1900 (não), 2024 (bissexto)
# ============================================================

ano = 2024

# TODO: verifique se o ano é bissexto e imprima

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
if bissexto:
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

