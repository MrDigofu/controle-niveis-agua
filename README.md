# Controle de Níveis de Água

Projeto em Python desenvolvido para simular o monitoramento do nível de água de um reservatório pelo terminal. Cada nível apresenta uma mensagem com uma cor específica, utilizando a biblioteca **Colorama**.

## Objetivo

Praticar o uso de listas, funções, estruturas condicionais, laços de repetição e bibliotecas Python.

## Níveis monitorados

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Tecnologias utilizadas

- Python 3
- Colorama

## Como executar

1. Instale o Python 3.
2. Abra o terminal na pasta do projeto.
3. Instale a dependência:

   ```bash
   pip install colorama
   ```

4. Execute o programa:

   ```bash
   python controle_agua.py
   ```

## Estrutura do projeto

```text
controle-niveis-agua/
├── controle_agua.py
└── README.md
```

## Funcionamento

O programa armazena as mensagens em uma lista. A função `definir_cor()` recebe o número do nível e retorna a cor correspondente. Em seguida, um laço `for` percorre a lista e apresenta cada mensagem colorida no terminal. O estilo é restaurado após cada mensagem com `Style.RESET_ALL`.

## Observação

Esta é uma simulação didática com mensagens predefinidas no código. Não realiza leitura de sensores nem monitora um reservatório real.
