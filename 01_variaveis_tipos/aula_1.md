# Aula 1 — Variáveis e Tipos

## O que é uma variável?

Pense em uma variável como uma **caixa com uma etiqueta**. Você coloca um valor dentro da caixa e coloca um nome nela para encontrar depois.

```python
nome = "Maria"
idade = 22
altura = 1.65
estudante = True
```

Aqui, `nome` é a etiqueta, e `"Maria"` é o conteúdo da caixa.

## Tipos primitivos em Python

Python trabalha com alguns tipos básicos de dados:

| Tipo | Exemplo | Descrição |
|------|---------|-----------|
| `int` | `42`, `-3`, `0` | Números inteiros |
| `float` | `3.14`, `-0.5`, `1e3` | Números decimais (ponto flutuante) |
| `str` | `"olá"`, `'mundo'` | Texto (string) |
| `bool` | `True`, `False` | Valores lógicos (verdadeiro/falso) |

### Verificando o tipo com `type()`

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("olá"))     # <class 'str'>
print(type(True))      # <class 'bool'>
```

## Conversão entre tipos

Você pode converter valores de um tipo para outro:

```python
# String para inteiro
idade_str = "22"
idade_int = int(idade_str)   # 22

# Inteiro para float
nota = int(8.9)              # 8 (trunca, não arredonda)

# Float para string
pi_str = str(3.14)           # "3.14"

# Inteiro para bool
print(bool(0))    # False
print(bool(1))    # True
print(bool(""))   # False
print(bool("a"))  # True
```

> **Regra:** Valores "vazios" (`0`, `0.0`, `""`, `None`) convertidos para `bool` resultam em `False`. Todo o resto é `True`.

## Input e Output

### `print()` — Saída de dados

```python
print("Olá, mundo!")
print(42)
print("A soma é:", 10 + 5)
```

### f-strings — Formatação elegante

```python
nome = "Ana"
idade = 20
print(f"Meu nome é {nome} e tenho {idade} anos.")
# Saída: Meu nome é Ana e tenho 20 anos.

# Expressões dentro de f-strings
preco = 49.9
print(f"O preço com 10% de desconto é R$ {preco * 0.9:.2f}")
# Saída: O preço com 10% de desconto é R$ 44.91
```

### `input()` — Entrada de dados

```python
nome = input("Qual seu nome? ")
print(f"Olá, {nome}!")

# input() SEMPRE retorna string — converta se precisar de número
idade = int(input("Qual sua idade? "))
```

## Operadores aritméticos

| Operador | Exemplo | Resultado |
|----------|---------|-----------|
| `+` | `10 + 3` | `13` |
| `-` | `10 - 3` | `7` |
| `*` | `10 * 3` | `30` |
| `/` | `10 / 3` | `3.333...` |
| `//` | `10 // 3` | `3` (divisão inteira) |
| `%` | `10 % 3` | `1` (resto da divisão) |
| `**` | `2 ** 3` | `8` (potenciação) |

```python
# Exemplo prático: calcular área de um círculo
raio = 5
pi = 3.14159
area = pi * raio ** 2
print(f"Área = {area:.2f}")
```

## Operadores de comparação

| Operador | Significado | Exemplo |
|----------|-------------|---------|
| `==` | Igual a | `5 == 5` → `True` |
| `!=` | Diferente de | `5 != 3` → `True` |
| `<` | Menor que | `3 < 5` → `True` |
| `>` | Maior que | `5 > 3` → `True` |
| `<=` | Menor ou igual | `3 <= 3` → `True` |
| `>=` | Maior ou igual | `5 >= 3` → `True` |

> **Atenção:** `=` é atribuição (guarda valor), `==` é comparação (verifica igualdade).

## Nomes de variáveis — Boas práticas

```python
# CORRETO (snake_case)
nome_completo = "João Silva"
temperatura_corporal = 36.5
numero_de_fotons = 1000

# EVITE
NomeCompleto = "João Silva"   # PascalCase (reservado para classes)
n = "João Silva"               # nome sem significado
numero-de-fotons = 1000        # hífen não é permitido
```

**Regras:**
- Comece com letra ou `_` (nunca com número)
- Use apenas letras, números e `_`
- Case-sensitive: `Nome` ≠ `nome` ≠ `NOME`
- Palavras reservadas não podem ser usadas: `if`, `for`, `class`, `return`, etc.

## Resumo rápido

```python
# Declaração
nome = "Python"          # str
versao = 3               # int
pi = 3.14                # float
ativo = True             # bool

# Conversão
numero = int("42")       # str → int
texto = str(3.14)        # float → str

# Operações
soma = 10 + 5            # 15
potencia = 2 ** 10       # 1024
resto = 17 % 5           # 2

# f-string
print(f"{nome} {versao} — pi ≈ {pi}")
```

---

**Exercício:** Veja o arquivo `exercicio_1.py` nesta mesma pasta para praticar.
