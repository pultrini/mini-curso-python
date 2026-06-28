"""
Exercício: Decaimento Radioativo
Objetivo: Calcular a atividade restante de um material radioativo ao longo do tempo.

Fórmula: N(t) = N₀ * exp(-λ * t)
Atividade: A(t) = λ * N(t)
Meia-vida: t½ = ln(2) / λ
"""

import math

def calcular_atividade(N0, lambda_dec, t):
    """Calcula N(t) = N₀ * exp(-λ * t).

    Parâmetros:
        N0 (float): número inicial de átomos
        lambda_dec (float): constante de decaimento (s⁻¹)
        t (float): tempo decorrido (s)

    Retorna:
        float: número de átomos no tempo t
    """
    # TODO: implemente a fórmula do decaimento exponencial
    N = math.exp(-lambda_dec * t) * N0
    return N



def calcular_meia_vida(lambda_dec):
    """Calcula a meia-vida a partir da constante de decaimento.

    Parâmetros:
        lambda_dec (float): constante de decaimento (s⁻¹)

    Retorna:
        float: meia-vida (s)
    """
    # TODO: implemente t½ = ln(2) / λ
    t_1_2 = math.log(2) / lambda_dec
    pass


def simular_decaimento(N0, lambda_dec, tempo_total, passo):
    """Simula o decaimento ao longo do tempo, imprimindo a cada passo.

    Parâmetros:
        N0 (float): átomos iniciais
        lambda_dec (float): constante de decaimento (s⁻¹)
        tempo_total (float): tempo total de simulação (s)
        passo (float): intervalo entre medições (s)
    """
    # TODO: use um loop para imprimir N(t) a cada 'passo' segundos
    # Dica: use range() com float convertendo para int, ou um while
    for t in range(0, tempo_total, passo):
        N = calcular_atividade(N0, lambda_dec, t)
        print(f"No tempo {t} temos a atividade {N}")
        N0 = N


# ============================================================
# Teste seu código abaixo
# ============================================================

if __name__ == "__main__":
    # Dados: Tc-99m (meia-vida ≈ 6.01 horas)
    N0 = 1e12                          # átomos iniciais
    meia_vida_horas = 6.01             # horas
    meia_vida_seg = meia_vida_horas * 3600  # converter para segundos
    lambda_tc = math.log(2) / meia_vida_seg # constante de decaimento

    # 1) Calcule e imprima a meia-vida
    t_half = calcular_meia_vida(lambda_tc)
    print(f"Meia-vida: {t_half / 3600:.2f} horas")

    # 2) Calcule quantos átomos restam após 12 horas
    t = 12 * 3600  # 12 horas em segundos
    restantes = calcular_atividade(N0, lambda_tc, t)
    print(f"Após 12h: {restantes:.2e} átomos")

    # 3) Simule o decaimento a cada 1 hora por 24 horas
    print("\nSimulação (a cada 1h por 24h):")
    print("-" * 30)
    simular_decaimento(N0, lambda_tc, 24 * 3600, 3600)
