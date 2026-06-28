"""
Exercício: Cálculo de Meia-vida
Objetivo: Calcular meia-vida, constante de decaimento e atividade.

Fórmulas:
    t½ = ln(2) / λ
    λ = ln(2) / t½
    A(t) = A₀ * exp(-λ * t)
    A = λ * N
"""

import math

# Isótopos comuns em medicina
ISOTOPOS = {
    "Tc-99m": {"meia_vida_h": 6.01, "uso": "Cintilografia"},
    "I-131":  {"meia_vida_h": 8.02 * 24, "uso": "Terapia de tireoide"},
    "F-18":   {"meia_vida_h": 109.8 / 60, "uso": "PET"},
    "Co-60":  {"meia_vida_h": 5.27 * 365.25 * 24, "uso": "Radioterapia"},
    "Cs-137": {"meia_vida_h": 30.17 * 365.25 * 24, "uso": "Braquiterapia"},
}


def meia_vida_para_lambda(meia_vida):
    """Calcula λ a partir da meia-vida: λ = ln(2) / t½.

    Parâmetros:
        meia_vida (float): meia-vida em horas

    Retorna:
        float: constante de decaimento (h⁻¹)
    """
    # TODO: implemente λ = ln(2) / t½

    lambda_dec = math.log(2) / meia_vida
    return lambda_dec



def lambda_para_meia_vida(lambda_dec):
    """Calcula t½ a partir de λ: t½ = ln(2) / λ.

    Parâmetros:
        lambda_dec (float): constante de decaimento (h⁻¹)

    Retorna:
        float: meia-vida em horas
    """
    # TODO: implemente t½ = ln(2) / λ

    meia_vida = math.log(2) / lambda_dec



def atividade_restante(A0, lambda_dec, t):
    """Calcula A(t) = A₀ * exp(-λ * t).

    Parâmetros:
        A0 (float): atividade inicial (Bq)
        lambda_dec (float): constante de decaimento (h⁻¹)
        t (float): tempo (h)

    Retorna:
        float: atividade no tempo t (Bq)
    """
    # TODO: implemente a fórmula
    A = A0 * math.exp(lambda_dec*t)
    return A


def tempo_para_atividade(A0, A_final, lambda_dec):
    """Calcula o tempo necessário para atingir uma atividade específica.

    De A(t) = A₀ * exp(-λt), isole t:
    t = -ln(A/A₀) / λ = ln(A₀/A) / λ

    Parâmetros:
        A0 (float): atividade inicial (Bq)
        A_final (float): atividade desejada (Bq)
        lambda_dec (float): constante de decaimento (h⁻¹)

    Retorna:
        float: tempo necessário (h)
    """
    # TODO: implemente t = ln(A₀/A) / λ

    t = math.log(A0/A_final) / lambda_dec
    return t


def listar_isotopos():
    """Imprime uma tabela com os isótopos disponíveis."""
    print(f"{'Isótopo':<10} {'Meia-vida (h)':<15} {'λ (h⁻¹)':<15} {'Uso'}")
    print("-" * 60)
    for nome, dados in ISOTOPOS.items():
        tv = dados["meia_vida_h"]
        lam = meia_vida_para_lambda(tv)
        print(f"{nome:<10} {tv:<15.2f} {lam:<15.6f} {dados['uso']}")


# ============================================================
# Teste seu código abaixo
# ============================================================

if __name__ == "__main__":
    # 1) Listar isótopos
    print("Isótopos médicos:")
    listar_isotopos()

    # 2) Calcular λ do Tc-99m
    meia_vida_tc = ISOTOPOS["Tc-99m"]["meia_vida_h"]
    lambda_tc = meia_vida_para_lambda(meia_vida_tc)
    print(f"\nTc-99m: λ = {lambda_tc:.6f} h⁻¹")

    # 3) Atividade restante após 24h (início: 1 GBq)
    A0 = 1e9  # 1 GBq em Bq
    t = 24    # horas
    A = atividade_restante(A0, lambda_tc, t)
    print(f"Atividade após 24h: {A/1e6:.2f} MBq")

    # 4) Tempo para atingir 10 MBq
    A_final = 10e6  # 10 MBq
    tempo = tempo_para_atividade(A0, A_final, lambda_tc)
    print(f"Tempo para atingir 10 MBq: {tempo:.2f} h ({tempo/24:.1f} dias)")
