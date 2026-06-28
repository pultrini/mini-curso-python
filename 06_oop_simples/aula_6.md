# Aula 6 — OOP Simples (Programação Orientada a Objetos)

## O que é OOP?

Programação Orientada a Objetos organiza o código em **objetos** que combinam dados (atributos) e comportamentos (métodos).

Pense assim:
- **Classe** = molde (receita de bolo)
- **Objeto** = instância (bolo feito a partir do molde)

## Criando uma classe básica

```python
class Paciente:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

# Criando objetos (instâncias)
p1 = Paciente("Ana", 25, 60.5)
p2 = Paciente("João", 30, 75.0)

print(p1.nome)   # Ana
print(p2.idade)  # 30
```

> `__init__` é o **construtor** — executado automaticamente ao criar o objeto. `self` refere-se ao próprio objeto.

## Métodos

Métodos são funções que pertencem à classe:

```python
class Paciente:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def classificacao_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc < 25:
            return "Normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidade"

ana = Paciente("Ana", 25, 60, 1.65)
print(f"IMC de {ana.nome}: {ana.calcular_imc():.1f}")
print(f"Classificação: {ana.classificacao_imc()}")
```

## Atributos de instância vs classe

```python
class Isotopo:
    # Atributo de classe (compartilhado por todas as instâncias)
    tipo = "radioativo"

    def __init__(self, nome, meia_vida):
        # Atributo de instância (único para cada objeto)
        self.nome = nome
        self.meia_vida = meia_vida

tc99m = Isotopo("Tc-99m", 6.01)
i131 = Isotopo("I-131", 8.02)

print(tc99m.tipo)  # radioativo
print(i131.tipo)   # radioativo
```

## Herança

Uma classe pode **herdar** atributos e métodos de outra:

```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        return f"{self.marca} {self.modelo}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)  # chama o __init__ da classe pai
        self.portas = portas

    def descricao(self):
        return f"{super().descricao()}, {self.portas} portas"

meu_carro = Carro("Toyota", "Corolla", 4)
print(meu_carro.descricao())  # Toyota Corolla, 4 portas
```

> `super()` acessa métodos da classe pai. A classe filha pode **sobrescrever** métodos.

### Exemplo em física médica

```python
class Detector:
    def __init__(self, sensibilidade):
        self.sensibilidade = sensibilidade

    def detectar(self, intensidade):
        return intensidade * self.sensibilidade

class DetectorCintilacao(Detector):
    def __init__(self, sensibilidade, cristal):
        super().__init__(sensibilidade)
        self.cristal = cristal

    def detectar(self, intensidade):
        sinal = super().detectar(intensidade)
        return f"Sinal no {self.cristal}: {sinal:.2f}"

det = DetectorCintilacao(0.85, "NaI(Tl)")
print(det.detectar(100))  # Sinal no NaI(Tl): 85.00
```

## `__str__` e `__repr__`

```python
class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Paciente: {self.nome}, {self.idade} anos"

    def __repr__(self):
        return f"Paciente('{self.nome}', {self.idade})"

p = Paciente("Ana", 25)
print(p)           # Paciente: Ana, 25 anos  (usado por print())
print(repr(p))     # Paciente('Ana', 25)     (usado no console/debug)
```

> `__str__` é para o usuário final. `__repr__` é para o desenvolvedor (debug).

## Encapsulamento básico

Em Python, não existe `private` como em Java/C++. Usamos convenções:

```python
class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo      # _ = "protegido" (não acesse diretamente)
        self.__senha = None      # __ = "privado" (name mangling)

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return True
        return False
```

> `_` é uma **convenção** (avisa: "não acesse diretamente"). `__` causa *name mangling* (Python renomeia o atributo internamente).

## Métodos estáticos e de classe

```python
class ConstantesFisicas:
    c = 3e8           # velocidade da luz (m/s)
    h = 6.626e-34     # constante de Planck (J·s)
    kB = 1.381e-23    # constante de Boltzmann (J/K)

    @staticmethod
    def energia_foton(comprimento_onda):
        """E = hc/λ"""
        return ConstantesFisicas.h * ConstantesFisicas.c / comprimento_onda

    @classmethod
    def info(cls):
        return f"c = {cls.c} m/s"

print(ConstantesFisicas.energia_foton(500e-9))  # ~3.97e-19 J
print(ConstantesFisicas.info())
```

## Resumo

```python
# Classe básica
class NomeClasse:
    def __init__(self, atributos):
        self.atributo = atributo

    def metodo(self):
        return resultado

# Herança
class Filha(Pai):
    def __init__(self, ...):
        super().__init__(...)

# Métodos especiais
__init__    # construtor
__str__     # representação para print()
__repr__    # representação para debug

# Convenções de encapsulamento
_atributo   # protegido (não acesse fora da classe)
__atributo  # privado (name mangling)
```

---

**Exercício:** Veja o arquivo `exercicio_6.py` nesta mesma pasta para praticar.
