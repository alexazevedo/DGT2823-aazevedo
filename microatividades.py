import pandas as pd

df = pd.read_csv('dados.csv', sep=';', engine='python')
print(df)

print("\n")

subconjunto = df[['Duration', 'Pulse', 'Calories']]
print(subconjunto)

print("\n")

pd.options.display.max_rows = 9999
print(".....")
print(df.to_string())

print("\n")

print(df.head(10))

print("\n")

print(df.tail(10))

print("\n")

print(df.info())
