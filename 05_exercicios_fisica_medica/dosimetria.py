"""
Exercício: Dosimetria
Objetivo: Calcular dose absorvida, equivalente de dose e verificar limites de segurança.

Dose absorvida: D = dE/dm [Gray = J/kg]
Equivalente de dose: H = D × wR [Sievert]
Dose efetiva: E = Σ(wT × HT)
"""

# Fatores de ponderação por tipo de radiação (ICRP 103)
W_R = {
    "foton": 1,
    "eletron": 1,
    "proton": 2,
    "neutron": 5,      # simplificado (na realidade depende da energia)
    "alfa": 20,
}

# Limites anuais de dose (mSv)
LIMITE_PUBLICO = 1.0       # mSv/ano (excluindo radiação natural)
LIMITE_TRABALHADOR = 20.0  # mSv/ano (média de 5 anos)


def calcular_dose_absorvida(energia, massa):
    """Calcula D = energia / massa [Gy].

    Parâmetros:
        energia (float): energia depositada (J)
        massa (float): massa do tecido (kg)

    Retorna:
        float: dose absorvida em Gray
    """
    # TODO: implemente D = energia / massa
    D = energia/massa
    return D


def calcular_equivalente_dose(dose_Gy, tipo_radiacao):
    """Calcula H = D × wR [Sv].

    Parâmetros:
        dose_Gy (float): dose absorvida em Gray
        tipo_radiacao (str): tipo de radiação (chave do dicionário W_R)

    Retorna:
        float: equivalente de dose em Sievert

    Levanta:
        ValueError: se o tipo de radiação não for reconhecido
    """
    # TODO: use o dicionário W_R para obter o fator wR
    # Se o tipo não existir, levante ValueError

    H = dose_Gy * W_R[tipo_radiacao]
    return H


def verificar_limite(dose_mSv, tipo="publico"):
    """Verifica se a dose está dentro do limite permitido.

    Parâmetros:
        dose_mSv (float): dose em milisievert
        tipo (str): "publico" ou "trabalhador"

    Retorna:
        str: "DENTRO DO LIMITE" ou "ACIMA DO LIMITE"
    """
    # TODO: compare dose_mSv com LIMITE_PUBLICO ou LIMITE_TRABALHADOR
    dose_trabalhador = "DENTRO DO LIMITE" if dose_mSv < LIMITE_TRABALHADOR else "ACIMA DO LIMITE"
    dose_publico = "DENTRO DO LIMITE" if dose_mSv < LIMITE_PUBLICO else "ACIMA DO LIMITE"

    print(f"dado a dose {dose_mSv} para um trabalhador ele esta {dose_trabalhador} e para o público está {dose_publico}")


def converter_sievert(valor, de, para):
    """Converte entre unidades de Sievert.

    Parâmetros:
        valor (float): valor a converter
        de (str): unidade de origem ("Sv", "mSv", "μSv", "rem")
        para (str): unidade de destino ("Sv", "mSv", "μSv", "rem")

    Retorna:
        float: valor convertido

    Tabela de conversão (para Sv):
        1 Sv  = 1 Sv
        1 mSv = 0.001 Sv
        1 μSv = 0.000001 Sv
        1 rem = 0.01 Sv
    """
    # TODO: crie um dicionário de fatores de conversão para Sv
    # Converta: valor → Sv → unidade destino

    fatores = {
        "Sv": 1,
        "mSv": 0.001,
        "μSv": 0.000001,
        "rem": 0.01
    }
    if de not in fatores or para not in fatores:
        print("Não há nada dentro dos fatores configurados")
        return
    valor_em_sv = valor * fatores[de]
    valor_convertido = valor_em_sv /fatores[para]

    print(f"o valor foi convertido para {valor_convertido}. Ele era {valor_em_sv}")
    

# ============================================================
# Teste seu código abaixo
# ============================================================

if __name__ == "__main__":
    # 1) Dose absorvida: 0.5 J depositados em 0.01 kg de tecido
    dose = calcular_dose_absorvida(0.5, 0.01)
    print(f"Dose absorvida: {dose:.2f} Gy")

    # 2) Equivalente de dose para fótons e partículas alfa
    h_foton = calcular_equivalente_dose(dose, "foton")
    h_alfa = calcular_equivalente_dose(dose, "alfa")
    print(f"H (fótons): {h_foton:.2f} Sv")
    print(f"H (alfa):   {h_alfa:.2f} Sv")

    # 3) Verificar limites
    print(f"\nDose de 15 mSv para público: {verificar_limite(15, 'publico')}")
    print(f"Dose de 15 mSv para trabalhador: {verificar_limite(15, 'trabalhador')}")

    # 4) Conversões
    print(f"\n0.005 Sv = {converter_sievert(0.005, 'Sv', 'mSv'):.1f} mSv")
    print(f"500 mSv = {converter_sievert(500, 'mSv', 'Sv'):.2f} Sv")
    print(f"100 μSv = {converter_sievert(100, 'μSv', 'mSv'):.2f} mSv")
