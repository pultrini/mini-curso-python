"""
Exercício 4 — Funções
Complete os exercícios abaixo seguindo as instruções nos comentários.
"""

# ============================================================
# Exercício 4.1: Saudação personalizada
# Crie uma função saudacao(nome) que imprima "Olá, <nome>!"
# Chame a função com pelo menos 3 nomes diferentes
# ============================================================

# TODO: defina e chame a função

def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao("Alice")
saudacao("Bob")
saudacao("Charlie")

# ============================================================
# Exercício 4.2: Área do círculo
# Crie uma função area_circulo(raio) que RETORNE a área
# Fórmula: A = π × r²
# Use math.pi ou defina pi = 3.14159
# ============================================================

# TODO: defina a função e teste com raios 3, 5, 10

def area_circulo(raio):
    pi = 3.14159
    print(f"A área do círculo com raio {raio} é: {pi * (raio ** 2)}")
    return pi * (raio ** 2)

print(area_circulo(3))
print(area_circulo(5))
print(area_circulo(10))


# ============================================================
# Exercício 4.3: Maior de dois números
# Crie uma função maior(a, b) que retorne o maior valor
# Se forem iguais, retorne "Empate"
# ============================================================

# TODO: defina a função e teste com (3, 7), (10, 5), (4, 4)

def maior(a, b):
    if a > b:
        print(f"O maior número entre {a} e {b} é: {a}")
        return a
    elif b > a:
        print(f"O maior número entre {a} e {b} é: {b}")
        return b
    else:
        print(f"Os números {a} e {b} são iguais.")
        return "Empate"

maior(3, 7)
maior(10, 5)
maior(4, 4)

# ============================================================
# Exercício 4.4: Classificador de IMC
# Crie uma função classificar_imc(peso, altura) que:
#   1. Calcule o IMC (peso / altura²)
#   2. Retorne uma tupla (imc, classificacao)
# Classificações:
#   < 18.5: "Abaixo do peso"
#   18.5-24.9: "Normal"
#   25-29.9: "Sobrepeso"
#   >= 30: "Obesidade"
# ============================================================

# TODO: defina a função e teste com diferentes pesos/alturas
def classificar_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        classificacao = "Normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    print(f"IMC: {imc:.2f}, Classificação: {classificacao}")
    return (imc, classificacao)

# ============================================================
# Exercício 4.5: Contador de vogais
# Crie uma função contar_vogais(texto) que retorne
# a quantidade de vogais (a, e, i, o, u) no texto
# Ignore maiúsculas/minúsculas
# ============================================================

# TODO: defina a função e teste com "Programacao Python"
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    print(f"O texto '{texto}' contém {contador} vogais.")
    return contador

# ============================================================
# Exercício 4.6: Potência recursiva
# Crie uma função potencia(base, exp) que calcule base^exp
# usando recursão (não use **)
# Caso base: exp == 0 → retorna 1
# Caso recursivo: base * potencia(base, exp - 1)
# ============================================================

# TODO: defina a função recursiva e teste com potencia(2, 10)
def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)

# ============================================================
# Exercício 4.7: Função com valor padrão
# Crie uma função calcular_preco(preco, desconto=10) que:
#   - Receba o preço e um desconto em % (padrão 10%)
#   - Retorne o preço com desconto aplicado
# ============================================================

# TODO: defina e teste com (100), (100, 20), (50, 5)
def calcular_preco(preco, desconto=10):
    preco_final = preco * (1 - desconto / 100)
    print(f"Preço original: {preco}, Desconto: {desconto}%, Preço final: {preco_final}")
    return preco_final

calcular_preco(100)
calcular_preco(100, 20)
calcular_preco(50, 5)


# ============================================================
# Exercício 4.8: Lista de aprovados
# Crie uma função verificar_aprovados(notas, media_min=6.0) que:
#   - Receba uma lista de notas
#   - Retorne uma lista com as notas >= media_min
# Use o que aprendeu sobre listas e loops
# ============================================================

notas = [4.5, 7.0, 8.5, 3.0, 6.0, 9.0, 5.5]

# TODO: defina a função e teste com a lista 'notas'

def verificar_aprovados(notas, media_min=6.0):
    aprovados = []
    for nota in notas:
        if nota >= media_min:
            aprovados.append(nota)
    print(f"Notas aprovadas (>= {media_min}): {aprovados}")
    return aprovados

verificar_aprovados(notas)
