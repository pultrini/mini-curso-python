# Aula 2 — Fluxo de Código

## Por que precisamos de fluxo?

Até agora, nossos programas executam linha por linha, de cima para baixo. Mas na vida real, tomamos decisões: "Se chover, levo guarda-chuva. Senão, uso óculos de sol."

Em Python, controlamos o fluxo com **condicionais**.

## `if` — A decisão mais básica

```python
temperatura = 38.5

if temperatura > 37.5:
    print("Febre detectada!")
```

> **Regra de ouro:** O bloco dentro do `if` só executa se a condição for `True`. A indentação (4 espaços) define o que pertence ao bloco.

## `if` / `else` — Duas opções

```python
temperatura = 36.8

if temperatura > 37.5:
    print("Febre detectada!")
else:
    print("Temperatura normal.")
```

## `if` / `elif` / `else` — Múltiplas opções

```python
nota = 7.5

if nota >= 9.0:
    print("A — Excelente")
elif nota >= 7.0:
    print("B — Bom")
elif nota >= 5.0:
    print("C — Regular")
else:
    print("D — Insuficiente")
```

> Python avalia de cima para baixo. Quando encontra a primeira condição `True`, executa aquele bloco e **pula** todo o resto.

## Blocos aninhados

```python
idade = 25
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("Pode dirigir.")
    else:
        print("Precisa tirar a carteira.")
else:
    print("Menor de idade, não pode dirigir.")
```

> Dica: Evite muitos níveis de aninhamento (máximo 2-3). Se ficar complexo, refatore.

## Operadores lógicos

| Operador | Significado | Exemplo |
|----------|-------------|---------|
| `and` | E (ambos) | `x > 0 and x < 10` |
| `or` | OU (pelo menos um) | `x < 0 or x > 100` |
| `not` | Negação | `not (x > 5)` |

```python
ph = 7.2

if 6.5 <= ph <= 8.5:
    print("pH dentro da faixa aceitável para água potável.")

# Equivalente com 'and':
if ph >= 6.5 and ph <= 8.5:
    print("pH aceitável.")
```

### Combinações complexas

```python
temperatura = 39.0
dor_cabeca = True

if temperatura > 37.5 and dor_cabeca:
    print("Possível infecção — procurar médico.")

if not dor_cabeca:
    print("Sem dor de cabeça.")
```

## Truthy e Falsy

Python trata alguns valores como `False` implicitamente:

```python
# Falsy (avaliado como False)
bool(0)       # False
bool(0.0)     # False
bool("")      # False
bool([])      # False
bool(None)    # False

# Truthy (avaliado como True)
bool(1)       # True
bool("oi")    # True
bool([1,2])   # True
bool(-3.14)   # True
```

Isso é útil em verificações rápidas:

```python
nome = input("Nome: ")

if nome:  # Se não for string vazia
    print(f"Olá, {nome}!")
else:
    print("Nome não informado.")
```

## Condições em uma linha (ternário)

```python
idade = 20
status = "maior" if idade >= 18 else "menor"
print(status)  # "maior"
```

## `match` / `case` (Python 3.10+)

Para quem tem Python 3.10 ou superior, existe uma alternativa ao `elif` encadeado:

```python
dia = "segunda"

match dia:
    case "segunda":
        print("Início da semana!")
    case "sexta":
        print("Sextou!")
    case "sábado" | "domingo":
        print("Fim de semana!")
    case _:
        print("Dia normal.")
```

> `case _` é o curinga (equivalente ao `else`).

## Erros comuns

```python
# ERRO: = ao invés de ==
x = 5
if x = 5:    # SyntaxError!
    print("oi")

# CORRETO:
if x == 5:
    print("oi")
```

```python
# ERRO: esquecer os dois pontos
if x > 3     # SyntaxError!
    print("oi")

# CORRETO:
if x > 3:
    print("oi")
```

```python
# ERRO: indentação inconsistente
if x > 3:
print("oi")      # IndentationError!

# CORRETO:
if x > 3:
    print("oi")
```

## Resumo

```python
# if / elif / else
if condicao_1:
    bloco_1
elif condicao_2:
    bloco_2
else:
    bloco_3

# Operadores lógicos
and   # ambos verdadeiros
or    # pelo menos um verdadeiro
not   # inverte o valor

# Ternário
resultado = "sim" if condicao else "não"
```

---

**Exercício:** Veja o arquivo `exercicio_2.py` nesta mesma pasta para praticar.
