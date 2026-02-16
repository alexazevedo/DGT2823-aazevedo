import pandas as pd

dados = pd.read_csv('dados.csv', sep=';', engine='python')

print(dados.info())
print("\n")

print(dados.head(10))
print("\n")

print(dados.tail(10))
print("\n")

dados_copia = dados.copy()

dados_copia['Calories'] = dados_copia['Calories'].fillna(0)
print(dados_copia)
print("\n")

dados_copia['Date'] = dados_copia['Date'].fillna('1900/01/01')
print(dados_copia)
print("\n")

dados_copia['Date'] = dados_copia['Date'].astype(str)
dados_copia.loc[dados_copia['Date'] == '20201226', 'Date'] = "'2020/12/26'"

dados_copia['Date'] = dados_copia['Date'].replace('1900/01/01', pd.NA)
print(dados_copia)
print("\n")

dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], format="'%Y/%m/%d'", errors='coerce')
print(dados_copia)
print("\n")

dados_copia = dados_copia.dropna(subset=['Date'])
print(dados_copia)
