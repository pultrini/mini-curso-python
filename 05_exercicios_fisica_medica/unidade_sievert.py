"""
Exercício: Unidade Sievert e Conversões
Objetivo: Converter entre unidades de dose de radiação e calcular doses equivalentes.

Unidades:
    Gray (Gy) = J/kg (dose absorvida)
    Sievert (Sv) = Gy × wR (equivalente de dose)
    1 Sv = 1000 mSv = 1_000_000 μSv
    1 rem = 0.01 Sv
"""

# Fatores de ponderação (ICRP)
W_R = {
    "foton": 1,
    "eletron": 1,
    "proton": 2,
    "neutron": 5,
    "alfa": 20,
}

# Conversão para Sv (fator multiplicativo)
FATORES_SV = {
    "Sv": 1,
    "mSv": 0.001,
    "μSv": 0.000001,
    "rem": 0.01,
    "mrem": 0.00001,
}


def converter_para_sv(valor, unidade):
    """Converte um valor para Sievert.

    Parâmetros:
        valor (float): valor a converter
        unidade (str): unidade de origem ("Sv", "mSv", "μSv", "rem", "mrem")

    Retorna:
        float: valor em Sievert

    Levanta:
        ValueError: se a unidade não for reconhecida
    """
    # TODO: use o dicionário FATORES_SV
    pass


def converter_de_sv(valor_sv, unidade_destino):
    """Converte de Sievert para a unidade desejada.

    Parâmetros:
        valor_sv (float): valor em Sievert
        unidade_destino (str): unidade de destino

    Retorna:
        float: valor na unidade de destino
    """
    # TODO: divida pelo fator da unidade destino
    pass


def converter(valor, de, para):
    """Converte entre quaisquer unidades de dose.

    Parâmetros:
        valor (float): valor a converter
        de (str): unidade de origem
        para (str): unidade de destino

    Retorna:
        float: valor convertido
    """
    # TODO: converta para Sv primeiro, depois para a unidade destino
    pass


def dose_equivalente(dose_Gy, tipo_radiacao):
    """Calcula H = D × wR.

    Parâmetros:
        dose_Gy (float): dose absorvida em Gray
        tipo_radiacao (str): tipo de radiação

    Retorna:
        float: equivalente de dose em Sv
    """
    # TODO: multiplique pelo fator wR correspondente
    pass


def analise_exposicao(dose_mSv, tipo_pessoa="publico"):
    """Analisa se uma dose está dentro dos limites e retorna um relatório.

    Parâmetros:
        dose_mSv (float): dose em mSv
        tipo_pessoa (str): "publico" ou "trabalhador"

    Retorna:
        str: relatório com status e percentual do limite
    """
    limites = {"publico": 1.0, "trabalhador": 20.0}
    # TODO: calcule o percentual do limite e retorne uma string
    # Exemplo: "15.0 mSv | ACIMA DO LIMITE | 1500.0% do limite (1.0 mSv)"
    pass


# ============================================================
# Teste seu código abaixo
# ============================================================

if __name__ == "__main__":
    # 1) Conversões básicas
    print("=== Conversões ===")
    print(f"0.005 Sv  = {converter(0.005, 'Sv', 'mSv'):.1f} mSv")
    print(f"500 mSv   = {converter(500, 'mSv', 'Sv'):.2f} Sv")
    print(f"100 μSv   = {converter(100, 'μSv', 'mSv'):.2f} mSv")
    print(f"1 rem     = {converter(1, 'rem', 'mSv'):.1f} mSv")

    # 2) Dose equivalente
    print("\n=== Dose Equivalente ===")
    dose = 0.5  # Gy
    for tipo in W_R:
        h = dose_equivalente(dose, tipo)
        print(f"  {dose} Gy ({tipo}) = {h:.1f} Sv")

    # 3) Análise de exposição
    print("\n=== Análise de Exposições ===")
    doses = [0.5, 1.0, 1.5, 15, 25]
    for d in doses:
        print(f"  Público: {analise_exposicao(d, 'publico')}")
        print(f"  Trab.:   {analise_exposicao(d, 'trabalhador')}")
        print()
