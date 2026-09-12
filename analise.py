import pandas as pd

# 1. Carregar os dados
df = pd.read_csv("vendas.csv")

# 2. Engenharia de Dados: Criar colunas novas

df["faturamento"] = df["quantidade_vendida"] * df["valor_unitario"]
df["dia_semana"] = pd.to_datetime(df["data"], dayfirst=True).dt.day_name(locale='pt_BR')

print("📊 === RELATÓRIO DE ANÁLISE DE VENDAS ===\n")

# 3. Análise 1: Top 5 Produtos em Quantidade

print("1️⃣ Top 5 Produtos Mais Vendidos (Quantidade):")
print(df.groupby("produto")["quantidade_vendida"].sum().sort_values(ascending=False).head(5))
print("-" * 40)

# 4. Análise 2: Faturamento por Categoria

print("2️⃣ Faturamento Total por Categoria:")
print(df.groupby("categoria")["faturamento"].sum().sort_values(ascending=False))
print("-" * 40)

# 5. Análise 3: Volume por Dia da Semana

print("3️⃣ Volume de Vendas por Dia da Semana:")
print(df.groupby("dia_semana")["quantidade_vendida"].sum().sort_values(ascending=False).head(5))
print("=" * 40)