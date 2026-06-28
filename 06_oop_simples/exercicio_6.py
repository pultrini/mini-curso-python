"""
Exercício 6 — Programação Orientada a Objetos
Complete os exercícios abaixo seguindo as instruções nos comentários.
"""

# ============================================================
# Exercício 6.1: Classe Pessoa
# Crie uma classe Pessoa com:
#   - Atributos: nome, idade, email
#   - Método: apresentar() → "Olá, sou <nome>, tenho <idade> anos."
# Crie 2 objetos e chame apresentar() para cada um
# ============================================================

# TODO: crie a classe Pessoa e instancie 2 objetos


# ============================================================
# Exercício 6.2: Classe Retangulo
# Crie uma classe Retangulo com:
#   - Atributos: largura, altura
#   - Método: area() → retorna largura × altura
#   - Método: perimetro() → retorna 2 × (largura + altura)
#   - Método: __str__() → "Retangulo(largura=X, altura=Y)"
# ============================================================

# TODO: crie a classe e teste com largura=5, altura=3


# ============================================================
# Exercício 6.3: Classe ContaBancaria
# Crie uma classe ContaBancaria com:
#   - Atributo: _saldo (começa em 0)
#   - Método: depositar(valor) → adiciona ao saldo (se valor > 0)
#   - Método: sacar(valor) → subtrai do saldo (se saldo suficiente)
#   - Método: get_saldo() → retorna o saldo
# ============================================================

# TODO: crie a classe, deposite, saque e imprima o saldo


# ============================================================
# Exercício 6.4: Herança — Animal
# Crie uma classe Animal com:
#   - Atributos: nome, som
#   - Método: falar() → "<nome> faz <som>!"
# Crie classes filhas Cachorro e Gato que herdam de Animal
#   - Cachorro: som padrão "Au au"
#   - Gato: som padrão "Miau"
# ============================================================

# TODO: crie as classes e teste


# ============================================================
# Exercício 6.5: Classe Particula (física)
# Crie uma classe Particula com:
#   - Atributos: nome, massa (kg), carga (C), velocidade (m/s)
#   - Método: energia_cinetica() → retorna 0.5 × massa × velocidade²
#   - Método: momento() → retorna massa × velocidade
#   - Método: __str__() → "Particula(nome, m=X kg, q=Y C, v=Z m/s)"
# ============================================================

# TODO: crie a classe e teste com um elétron:
# m = 9.109e-31 kg, q = -1.602e-19 C, v = 1e6 m/s


# ============================================================
# Exercício 6.6: Herança — Detector
# Crie uma classe base Detector com:
#   - Atributo: sensibilidade
#   - Método: detectar(intensidade) → retorna intensidade × sensibilidade
# Crie uma classe filha DetectorGeiger(Detector) com:
#   - Atributo adicional: taxa_contagem (inicia em 0)
#   - Sobrescreva detectar(): incrementa taxa_contagem e retorna o sinal
#   - Método: get_taxa() → retorna taxa_contagem
# ============================================================

# TODO: crie as classes e simule 5 detecções
