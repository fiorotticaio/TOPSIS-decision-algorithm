# README

## Descrição dos Arquivos CSV

Este repositório contém três arquivos CSV que são usados como parâmetros para o programa `main.py`. A seguir, uma descrição detalhada de cada arquivo:

### matrix_d.csv

Cada linha deste arquivo representa uma opção. Cada coluna representa os parâmetros dessa opção em relação aos critérios. Os valores são separados por vírgulas.

### weights.csv

Cada linha deste arquivo contém a importância de cada parâmetro para o usuário, expressa em porcentagem, e se esse parâmetro é do tipo "quanto mais, melhor" (1) ou "quanto menos, melhor" (0). Os valores são separados por vírgulas.

### options.csv

Este arquivo contém o nome de cada uma das opções. Esses nomes serão usados para plotar as opções no gráfico final.

## Como Usar

1. Certifique-se de que os arquivos CSV estão no mesmo diretório que o arquivo `main.py`.
2. Execute o arquivo `main.py`.
3. O programa usará os dados dos arquivos CSV para calcular e plotar um gráfico com as opções.

## Exemplo de Uso

```bash
python main.py