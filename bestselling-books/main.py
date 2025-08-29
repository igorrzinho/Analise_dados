import pandas as pd 

df = pd.read_csv('bestsellers.csv')

# obter as 5 primeiras linhas 

print("primeiras linhas:")
print(df.head())
print("-"*150)

print("Formato da tabela:")
print("-"*150)
print(df.shape)
print("-"*150)

print("Nomes das colunas da tabela:")
print("-"*150)
print(df.columns)
print("-"*150)


print("Estatisticas da tabela:")
print("-"*150)
print(df.describe())
print("-"*150)

# ------------------------------
# removendo as linhas duplicadas

df.drop_duplicates(inplace=True)

# ------------------------------
# renomeando as colunas
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# ------------------------------
# Mudando o tipo de dado de uma coluna
df["Price"] = df["Price"].astype(float)


# ------------------------------
# analisando os autores
author_counts = df['Author'].value_counts()
print("-"*150)

print(author_counts)
print("-"*150)

# ------------------------------
# analisando as avaliacoes por genero
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print("-"*150)
print(avg_rating_by_genre)
print("-"*150)

# ------------------------------
# exporta os 10 autores mais vendidos
author_counts.head(10).to_csv("top_authors.csv")
# exporta as avaliacoes medias
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
