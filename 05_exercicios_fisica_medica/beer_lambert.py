"""
Exercício: Lei de Beer-Lambert
Objetivo: Calcular transmitância, absorbância e intensidade transmitida.

Fórmula: I = I₀ * exp(-μ * x)
Transmitância: T = I / I₀
Absorbância: A = -log₁₀(T)
"""

import math

def calcular_intensidade_transmitida(I0, mu, x):
    """Calcula I = I₀ * exp(-μ * x).

    Parâmetros:
        I0 (float): intensidade incidente
        mu (float): coeficiente de atenuação linear (cm⁻¹)
        x (float): espessura do material (cm)

    Retorna:
        float: intensidade transmitida
    """
    # TODO: implemente a fórmula de Beer-Lambert
    pass


def calcular_transmitancia(I0, I):
    """Calcula T = I / I₀.

    Parâmetros:
        I0 (float): intensidade incidente
        I (float): intensidade transmitida

    Retorna:
        float: transmitância (0 a 1)
    """
    # TODO: implemente T = I / I₀
    pass


def calcular_absorbancia(T):
    """Calcula A = -log₁₀(T).

    Parâmetros:
        T (float): transmitância

    Retorna:
        float: absorbância
    """
    # TODO: implemente A = -log₁₀(T)
    # Cuidado: T não pode ser 0 (log de 0 é indefinido)
    pass


def tabela_atenuacao(I0, mu, espessuras):
    """Imprime uma tabela com espessura, intensidade, transmitância e absorbância.

    Parâmetros:
        I0 (float): intensidade incidente
        mu (float): coeficiente de atenuação (cm⁻¹)
        espessuras (list): lista de espessuras em cm
    """
    # TODO: para cada espessura, calcule I, T e A e imprima uma linha da tabela
    # Formato sugerido: "x=0.50 cm | I=82.15 | T=0.8215 | A=0.085"
    pass


# ============================================================
# Teste seu código abaixo
# ============================================================

if __name__ == "__main__":
    # Dados: feixe de raios X atravessando tecido mole
    I0 = 100.0           # intensidade incidente (arbitrária)
    mu_tecido = 0.2      # coeficiente de atenuação (cm⁻¹)
    espessura = 5.0      # cm

    # 1) Calcule a intensidade transmitida
    I = calcular_intensidade_transmitida(I0, mu_tecido, espessura)
    print(f"Intensidade transmitida: {I:.2f}")

    # 2) Calcule transmitância e absorbância
    T = calcular_transmitancia(I0, I)
    A = calcular_absorbancia(T)
    print(f"Transmitância: {T:.4f}")
    print(f"Absorbância: {A:.4f}")

    # 3) Tabela para diferentes espessuras
    print("\nTabela de atenuação:")
    print("-" * 45)
    espessuras = [0.5, 1.0, 2.0, 5.0, 10.0]
    tabela_atenuacao(I0, mu_tecido, espessuras)
