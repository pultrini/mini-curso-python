"""
Exercício 3 — Ciclos e Paradas
Complete os exercícios abaixo seguindo as instruções nos comentários.
"""

# ============================================================
# Exercício 3.1: Contagem regressiva
# Use while para imprimir de 10 até 1, depois "Fogo!"
# ============================================================

# TODO: use while
i = 0
while i < 10:
    i += 1
    print(11 - i)
print("Fogo!")


# ============================================================
# Exercício 3.2: Soma acumulada
# Some todos os números de 1 a 100 usando for + range
# Imprima o resultado
# ============================================================

# TODO: use for e acumulador
soma = 0
for i in range(1, 101):
    soma += i
print("A soma de 1 a 100 é:", soma)

# ============================================================
# Exercício 3.3: Tabuada
# Peça um número ao usuário e imprima a tabuada de 1 a 10
# Formato: "7 x 1 = 7", "7 x 2 = 14", ...
# ============================================================

# TODO: use input() e for
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# ============================================================
# Exercício 3.4: Encontrar o primeiro múltiplo de 7
# Usando for, encontre e imprima o primeiro número entre 50 e 100
# que é múltiplo de 7. Use break.
# ============================================================

# TODO: use for e break

intervalo_inferior = input("Digite o limite inferior do intervalo: ")
intervalo_superior = input("Digite o limite superior do intervalo: ")

for i in range(int(intervalo_inferior), int(intervalo_superior) + 1):
    if i % 7 == 0:
        print(f"O primeiro múltiplo de 7 entre {intervalo_inferior} e {intervalo_superior} é: {i}")
        break



# ============================================================
# Exercício 3.5: Pular múltiplos de 3
# Imprima os números de 1 a 20, exceto os múltiplos de 3
# Use continue
# ============================================================

# TODO: use for e continue
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


# ============================================================
# Exercício 3.6: Fatorial
# Calcule o fatorial de um número digitado pelo usuário
# n! = n × (n-1) × ... × 2 × 1
# Use while ou for
# ============================================================

# TODO: peça o número com input() e calcule o fatorial

numero_fatorial = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for i in range(1, numero_fatorial + 1):
    fatorial *= i
print(f"O fatorial de {numero_fatorial} é: {fatorial}")


# ============================================================
# Exercício 3.7: Sequência de Fibonacci
# Imprima os N primeiros números da sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Peça N ao usuário
# ============================================================

# TODO: use input() e um loop para gerar a sequência
n = int(input("Digite o número de termos da sequência de Fibonacci: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


# ============================================================
# Exercício 3.8: Média de notas
# Peça notas ao usuário até digitar -1
# Calcule e imprima a média das notas digitadas
# ============================================================

# TODO: use while, acumulador e contador

while True:
    nota = float(input("Digite uma nota (ou -1 para sair): "))
    if nota == -1:
        break
    soma_notas += nota
    contador_notas += 1
print("A média das notas digitadas é:", soma_notas / contador_notas)
