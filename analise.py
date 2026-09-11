import pandas as pd

df =pd.read_csv("vendas.csv")

print(df.head(10))

#CRIAMOS UMA TABELA DE FATURAMENTO 
df["faturamento"] = (df["quantidade_vendida"] * df["valor_unitario"])

print(df.head(10))

print(df.groupby("produto")["quantidade_vendida"].sum().sort_values(ascending=False).head(10))

print(df.groupby("categoria")["faturamento"].sum().sort_values(ascending=False).head(10))

df["dia_semana"] = pd.to_datetime(df["data"], dayfirst=True).dt.day_name(locale = 'pt_BR')

print(df.groupby("dia_semana")["quantidade_vendida"].sum().sort_values(ascending=False).head(10))