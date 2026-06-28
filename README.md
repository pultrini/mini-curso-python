# Monitoria de Python

Repositório de estudos da monitoria de Python, com foco em aplicações de **Física Médica**.

## Pré-requisitos

- **Python 3.10+** instalado ([python.org](https://www.python.org/downloads/))
- Editor de código (VS Code recomendado — [code.visualstudio.com](https://code.visualstudio.com/))
- Conhecimentos básicos de programação (variáveis, lógica)

## Como usar

1. Siga os módulos **na ordem** (01 → 07)
2. Leia o arquivo `.md` de cada módulo (teoria)
3. Complete os exercícios nos arquivos `.py`
4. Rode os scripts com:
    Se for linux/macOs ou WSL
   ```bash
   python3 exercicio_1.py
   ```
   Se for windows
   ```bash
   python ./exercicio_1.py
   ``

## Módulos

| # | Módulo | Conteúdo |
|---|--------|----------|
| 01 | [Variáveis e Tipos](01_variaveis_tipos/aula_1.md) | Tipos primitivos, conversões, input/output, operadores |
| 02 | [Fluxo de Código](02_fluxo_codigo/aula_2.md) | if/elif/else, operadores lógicos, truthy/falsy |
| 03 | [Ciclos e Paradas](03_ciclos_paradas/aula_3.md) | while, for, range, break, continue |
| 04 | [Funções](04_funcoes/aula_4.md) | def, parâmetros, return, escopo, recursão |
| 05 | [Exercícios — Física Médica](05_exercicios_fisica_medica/aula_5.md) | Decaimento, Beer-Lambert, dosimetria, tomografia, Sievert |
| 06 | [OOP Simples](06_oop_simples/aula_6.md) | Classes, objetos, métodos, herança, encapsulamento |
| 07 | [Bibliotecas (NumPy)](07_bibliotecas/aula_7.md) | Arrays, operações vetorizadas, estatísticas, matrizes |

## Estrutura de arquivos

```
python_monitorias/
├── README.md                          ← você está aqui
├── 01_variaveis_tipos/
│   ├── aula_1.md                      # Teoria
│   └── exercicio_1.py                 # Exercício (template)
├── 02_fluxo_codigo/
│   ├── aula_2.md
│   └── exercicio_2.py
├── 03_ciclos_paradas/
│   ├── aula_3.md
│   └── exercicio_3.py
├── 04_funcoes/
│   ├── aula_4.md
│   └── exercicio_4.py
├── 05_exercicios_fisica_medica/
│   ├── aula_5.md                      # Teoria + contexto de física médica
│   ├── decaimento_radioativo.py       # Exercício template
│   ├── beer_lambert.py
│   ├── dosimetria.py
│   ├── tomografia.py
│   ├── half_life.py
│   └── unidade_sievert.py
├── 06_oop_simples/
│   ├── aula_6.md
│   └── exercicio_6.py
└── 07_bibliotecas/
    ├── aula_7.md
    └── exercicio_7.py
```

## Dicas de estudo

- **Não copie e cole** — digite o código para fixar a sintaxe
- **Leia os erros** — as mensagens de erro do Python são informativas
- **Teste hipóteses** — abra um terminal Python (`python3`) e experimente
- **Use `print()`** — para entender o que o código está fazendo
- **Complete os TODOs** — cada arquivo `.py` tem instruções nos comentários

## Instalação do NumPy (módulo 7)

```bash
pip install numpy
```

## Comandos úteis do terminal

```bash
python3 script.py          # rodar um script
python3 -i script.py       # rodar e manter o terminal aberto
python3                    # abrir o REPL interativo
```

## Lista de exercícios para praticar

Após completar todos os módulos, resolva estes exercícios:

### Nível 1 — Variáveis e Tipos
1. Calcule o IMC de uma pessoa (peça peso e altura via input)
2. Converta uma temperatura de Fahrenheit para Celsius
3. Calcule a velocidade média de uma partícula (distância / tempo)

### Nível 2 — Fluxo de Código
4. Classifique um número como positivo, negativo ou zero
5. Verifique se um caractere é vogal ou consoante
6. Calcule o preço com desconto progressivo (até 100: 0%, 100-500: 10%, acima 500: 20%)

### Nível 3 — Ciclos
7. Imprima todos os números primos até N
8. Calcule a série harmônica: 1 + 1/2 + 1/3 + ... + 1/N
9. Simule o decaimento radioativo hora a hora até a atividade cair abaixo de 1%

### Nível 4 — Funções
10. Crie uma função que calcule a distância entre dois pontos 2D
11. Crie uma função que retorne o fatorial e o número de combinações C(n,k)
12. Crie uma função recursiva para calcular a soma de uma lista

### Nível 5 — Física Médica
13. Calcule a dose absorvida em 5 frações de 2 Gy cada
14. Determine o tempo necessário para que o F-18 (PET) decaia a 10% da atividade inicial
15. Simule a atenuação de um feixe de raios X em 3 camadas de materiais diferentes
16. Converta uma exposição de 500 mSv para Gy (fótons), Sv e rem

### Nível 6 — OOP
17. Crie uma classe `Isotopo` com atributos e método para calcular atividade
18. Crie uma hierarquia `Detector` → `DetectorCintilacao` → `DetectorPET`
19. Crie uma classe `Paciente` com histórico de doses e método de dose efetiva total

### Nível 7 — NumPy
20. Crie uma matriz 10x10 com a tabuada (i × j)
21. Gere 1000 valores de dose normalmente distribuídos e calcule estatísticas
22. Implemente a multiplicação de matrizes manualmente e compare com `np.dot()`

---

Monitoria de Python — Física Médica
