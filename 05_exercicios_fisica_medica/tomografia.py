"""
Exercício: Tomografia Computadorizada (Backprojection)
Objetivo: Implementar retroprojeção simples em uma grade 2D.

Conceito: Cada projeção é "espalhada" de volta pela imagem ao longo
da direção de detecção. A soma de todas as retroprojeções forma
a imagem reconstruída.
"""

import math

def criar_grade(tamanho):
    """Cria uma grade 2D (lista de listas) preenchida com zeros.

    Parâmetros:
        tamanho (int): dimensão da grade (tamanho × tamanho)

    Retorna:
        list: grade 2D de zeros
    """
    # TODO: retorne uma lista de listas preenchida com 0.0
    pass


def projetar_pixel(x, y, angulo_graus):
    """Calcula a posição do pixel (x,y) na projeção para um dado ângulo.

    A projeção é: t = x*cos(θ) + y*sin(θ)

    Parâmetros:
        x (int): coordenada x do pixel
        y (int): coordenada y do pixel
        angulo_graus (float): ângulo de projeção em graus

    Retorna:
        float: posição t na projeção
    """
    # TODO: converta o ângulo para radianos e aplique a fórmula
    pass


def retroprojetar(grade, projecao, angulo_graus, centro):
    """Adiciona uma retroprojeção à grade.

    Para cada pixel (x,y) da grade:
    1. Calcule a posição t na projeção
    2. Arredonde t para o índice mais próximo
    3. Se o índice for válido, some o valor da projeção na grade

    Parâmetros:
        grade (list): grade 2D a ser atualizada
        projecao (list): valores da projeção 1D
        angulo_graus (float): ângulo da projeção em graus
        centro (int): índice central da grade
    """
    tamanho = len(grade)
    for y in range(tamanho):
        for x in range(tamanho):
            # TODO: calcule a posição t na projeção
            # Dica: use projetar_pixel(), ajustando para coordenadas centradas
            # x_rel = x - centro, y_rel = y - centro
            # Arredonde t para inteiro e some projecao[t] na grade se 0 <= t < len(projecao)
            pass


def imprimir_grade(grade):
    """Imprime a grade formatada, normalizada entre 0 e 9.

    Parâmetros:
        grade (list): grade 2D de floats
    """
    # TODO: encontre o valor máximo da grade
    # Para cada linha, normalize os valores para 0-9 e imprima
    # Dica: use round(valor / maximo * 9) para normalizar
    pass


# ============================================================
# Teste seu código abaixo
# ============================================================

if __name__ == "__main__":
    tamanho = 21
    centro = tamanho // 2
    num_angulos = 18

    # Crie a grade vazia
    grade = criar_grade(tamanho)

    # Simule um "fantoma" simples: um ponto no centro
    # Criamos projeções para cada ângulo
    for i in range(num_angulos):
        angulo = i * (180 / num_angulos)

        # Projeção de um ponto no centro (pico no centro da projeção)
        proj = [0.0] * tamanho
        proj[centro] = 100.0  # ponto branco no centro

        # TODO: use retroprojetar() para adicionar esta projeção à grade
        pass

    print("Imagem reconstruída (backprojection):")
    imprimir_grade(grade)

    # Desafio: tente com múltiplos pontos (ex: centro + deslocado)
    print("\nDesafio: implemente para um fantoma com 2 pontos!")
