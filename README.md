# Trabalho Prático da Disciplina DCC014 - Inteligência Artificial

Trabalho prático da disciplina de Inteligência Artificial, DCC014, da Universidade Federal de Juiz de Fora, desenvolvido no semestre 2026-1.

## Integrantes

- Nina Aguiar Ferreira
- Luiz Fernando de Melo Nogueira

## Formato de entrada

O formato de entrada estabelecido para o programa segue a especificação descrita nesta seção.

### Cabeçalho

A primeira linha deve conter as dimensões do labirinto como dois inteiros maiores que 0 e não mutuamente iguais a 1 separados por espaço

- Exemplos de linhas válidas:
  - `10 8` para um labirinto de 10 de altura por 8 de largura
  - `1 2` para um labirinto com apenas entrada e saída
  - `100 100` para um labirinto quadrado com 100 unidades de lado
- Exemplos de linhas inválidas:
- `0 0`
  - `1 1` inválido pois não há espaço para a entrada e a saída

### Corpo (estrutura real do labirinto)

As demais linhas devem seguir o que foi especificado na primeira linha e possuir apenas os caracteres abaixo

- `#` para paredes
- ` ` (espaço em branco) para espaços caminháveis (livres)
  - Não deve haver espaços caminháveis nas bordas do labirinto, ou seja, as bordas só podem conter paredes, a entrada ou a saída
- `E` para a entrada
  - Deve haver uma entrada e esta só pode ser posicionada em alguma extremidade do labirinto
- `S` para a saída
  - Analogamente, deve haver uma única saída e esta só pode ser posicionada em alguma extremidade do labirinto

Seguir o que foi especificado na primeira linha significa conter uniformemente o número de linhas e colunas especificado. Assim, as linhas abaixo são inválidas:

```md
E ######
#    S
```

Ao tentar executar o programa com um arquivo inválido uma mensagem de erro será impressa apontando qual foi o problema detectado
