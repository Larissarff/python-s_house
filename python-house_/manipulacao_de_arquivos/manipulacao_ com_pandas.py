import pandas as pd

# atribuindo o arquivo a uma variavel
arquivo = "C:/Users/Pichau/Downloads/Python/pythons_house/python-s_house-1/python-house_/manipulacao_de_arquivos/arquivos/salarios.csv"

# df = dataframe
df = pd.read_csv(arquivo)

# exibindo o data frame criado
print(df.head())

# separador visual
print('\n\n------------------------------------------------------\n\n')

# filtrando o data frame pela frequencia na coluna
print(df['Position Title'].value_counts())