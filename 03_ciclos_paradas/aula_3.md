# Aula 3 — Ciclos e Paradas

## O que é um ciclo?

Um ciclo (loop) repete um bloco de código **enquanto uma condição for verdadeira** ou **para cada item de uma sequência**. É essencial quando queremos evitar repetição manual.

## `while` — Repete enquanto a condição for verdadeira

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# Saída: 0, 1, 2, 3, 4
```

> **Cuidado:** Se a condição nunca se tornar `False`, o loop é infinito!

```python
# Loop infinito (NÃO faça isso sem uma saída)
while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta == "sair":
        break  # ← sai do loop
```

### Exemplo prático: média de notas até digitar -1

```python
soma = 0
quantidade = 0

nota = float(input("Digite a nota (-1 para encerrar): "))

while nota != -1:
    soma += nota
    quantidade += 1
    nota = float(input("Digite a nota (-1 para encerrar): "))

if quantidade > 0:
    print(f"Média: {soma / quantidade:.2f}")
else:
    print("Nenhuma nota digitada.")
```

## `for` — Iterando sobre uma sequência

```python
# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(f"Eu gosto de {fruta}.")
```

```python
# Iterando sobre uma string
for letra in "Python":
    print(letra)
# Saída: P, y, t, h, o, n
```

## `range()` — Gerando sequências numéricas

```python
# range(início, fim, passo)
# ATENÇÃO: o 'fim' NÃO é incluído

for i in range(5):
    print(i)        # 0, 1, 2, 3, 4

for i in range(2, 6):
    print(i)        # 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)        # 0, 2, 4, 6, 8

for i in range(5, 0, -1):
    print(i)        # 5, 4, 3, 2, 1
```

### Exemplo: tabuada

```python
numero = 7

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
```

## `break` — Saindo do loop

```python
for i in range(100):
    if i == 5:
        print("Cheguei em 5, parando!")
        break
    print(i)
# Imprime 0, 1, 2, 3, 4 e para
```

## `continue` — Pulando uma iteração

```python
for i in range(10):
    if i % 2 == 0:
        continue  # pula números pares
    print(i)
# Saída: 1, 3, 5, 7, 9
```

> `break` **encerra** o loop. `continue` **pula** para a próxima iteração.

## `else` em loops

Python permite um `else` após `for` ou `while`. Ele executa **apenas se o loop terminar naturalmente** (sem `break`):

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop terminou sem break!")  # ← executa, porque não houve break
```

```python
for i in range(5):
    if i == 3:
        break
else:
    print("Isso NÃO será impresso.")  # ← não executa, porque houve break
```

## Loops aninhados

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # nova linha ao final de cada linha da tabela
```

Saída:
```
(0, 0) (0, 1) (0, 2)
(1, 0) (1, 1) (1, 2)
(2, 0) (2, 1) (2, 2)
```

## Acumuladores e contadores

```python
# Contar quantos números pares existem de 1 a 100
pares = 0
for i in range(1, 101):
    if i % 2 == 0:
        pares += 1
print(f"Existem {pares} números pares de 1 a 100.")

# Somar todos os números de 1 a 100
soma = 0
for i in range(1, 101):
    soma += i
print(f"Soma: {soma}")
```

## Erros comuns

```python
# ERRO: loop infinito
x = 0
while x < 5:
    print(x)
    # esqueceu x += 1 → loop infinito!

# CORRETO:
x = 0
while x < 5:
    print(x)
    x += 1
```

```python
# ERRO: off-by-one (erro de 1)
for i in range(1, 5):
    print(i)  # 1, 2, 3, 4 — faltou o 5!

# CORRETO (se quiser incluir o 5):
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5
```

## Resumo

```python
# while — repete enquanto condição for True
while condicao:
    bloco

# for — itera sobre sequencia
for item in sequencia:
    bloco

# range(início, fim, passo)
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8

# break  — encerra o loop
# continue — pula para próxima iteração
# else — executa se não houve break
```

---

**Exercício:** Veja o arquivo `exercicio_3.py` nesta mesma pasta para praticar.
