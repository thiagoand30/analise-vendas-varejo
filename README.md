# 📊 Análise de Dados de Vendas no Varejo

## 🎯 Sobre o Projeto
Este projeto tem como objetivo analisar um dataset de vendas de uma loja fictícia, transformando dados brutos em **insights acionáveis** para a tomada de decisão gerencial. 

O foco é demonstrar a aplicação de conceitos de manipulação de dados (Data Wrangling) e análise exploratória para responder perguntas de negócio reais, como identificação de produtos campeões, rentabilidade por categoria e sazonalidade de vendas.

## 🛠️ Tecnologias Utilizadas
- **Python 3**: Linguagem principal para scripting e lógica.
- **Pandas**: Biblioteca para manipulação, limpeza e agregação de dados (DataFrames).
- **Git & GitHub**: Versionamento de código e documentação do projeto.

## 🔍 Análises Realizadas
O script `analise.py` executa as seguintes etapas:
1. **Preparação dos Dados**: Criação da coluna `faturamento` (quantidade × valor unitário) e conversão da coluna de data para extrair o dia da semana.
2. **Ranking de Produtos**: Identificação do Top 5 itens com maior volume de saída.
3. **Rentabilidade por Categoria**: Cálculo do faturamento total agrupado por categoria de produto.
4. **Sazonalidade Semanal**: Mapeamento do volume de vendas por dia da semana para otimização de escalas de trabalho.

## 💡 Principais Insights de Negócio
Com base nos dados processados, foram identificadas as seguintes tendências:
- **Campeão de Volume**: O produto `[Camiseta]` lidera em quantidade vendida (`[42]` unidades), atuando como possível produto de atração.
- **Motor de Receita**: A categoria `[Vestuário]` é a que gera o maior faturamento total (`R$ [4.403,70]`), demonstrando sua importância estratégica para o estoque.
- **Pico de Movimento**: Contrariando a intuição comum de que o sábado é o dia mais forte, os dados apontam `[Quinta-feira]` como o dia de maior volume de vendas, sugerindo a necessidade de reforço na equipe neste período.

## 🚀 Como Executar o Projeto
1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca Pandas via terminal: `pip install pandas`
3. Clone este repositório ou baixe os arquivos `analise.py` e `vendas.csv` para a mesma pasta.
4. Execute o script no terminal:
   ```bash
   python analise.py