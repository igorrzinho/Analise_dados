# analise de dados

link da base : [https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019?resource=download](https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019?resource=download)

o arquivo csv contem 550 livros e tem 7 colunas sendo elas:

- Name:  nome do livro
- Author:  Autor do livro
- User Rating: Avaliações do livro de 0.0 até 5.0
- Reviews: Numero de comentarios
- Price: Preço de 2020
- Year: Ano que foi classificado
- Genre: ficção ou nao ficção

# 1º parte: Instalar e importar o pandas e a base de dados

vamos começar com a instalação do pandas:

```bash
pip install pandas
```

# 2º parte: Importar o pandas e a base de dados

Agora vamos importar o pandas para nossa base de dados:

```python
import pandas as pd
```

## importar a base de dados

definimos que o dataframe é `df` , que vai receber os dados para usarmos nas análises   

```python
df = pd.read_csv('bestsellers.csv')
```

# 3º parte: explorar os dados

Vamos enternder como os dados estão 

pegar as 5 primeiras linhas:

```python
print(df.head())
```

![image.png](https://github.com/igorrzinho/Analise_dados/blob/main/bestselling-books/img/image.png?raw=true)

---

Para obter o formato da tabela:

```python
print(df.shape)
```

![image.png](https://github.com/igorrzinho/Analise_dados/blob/main/bestselling-books/img/image%201.png?raw=true)

550 linhas e 7 colunas

---

para obter os nomes das colunas da planilha

```python
print(df.columns)
```

![image.png](https://github.com/igorrzinho/Analise_dados/blob/main/bestselling-books/img/image%202.png?raw=true)

---

para ober as estatisticas para cada coluna

```python
print(df.describe())
```

![image.png](https://github.com/igorrzinho/Analise_dados/blob/main/bestselling-books/img/image%203.png?raw=true)

# 4º parte: Limpar e formatar os dados

Agora que entendemos como funciona a tabela vamos mudar algumas coisas

Vamos remover as linhas duplicadas :

```python
df.drop_duplicates(inplace=True)
```

como definimos o `inplace` como `True` ele vai fazer as alterações no proprio `DataFrame`

---

## Renomear colunas

Para renomear as colunas usamos a função `rename()` , para deixar mais intuitiva

vamos mudar o Name para Title, Year para Publication Year e User Rating para Rating

```python
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
```

---

## Convertendo tipos de dados

para converter um tipo de dado usamos a função `astype()` 

Vamos converter a coluna `Price` para o formato `float`

```python
df["Price"] = df["Price"].astype(float)
```

# 5º parte: Análise

Agora que limpamos nossa base de dados vamos análisar os codigos

## Popularidade do autor

Analisando a coluna autores podemos ter uma melhor visualização dos autores mais vendidos

Vamos selecionar a coluna `Author` usando o `value_counts()`  e colocar esse valor numa variavel

```python
author_counts = df['Author'].value_counts()
print(author_counts)
```

![image.png](https://github.com/igorrzinho/Analise_dados/blob/main/bestselling-books/img/image%204.png?raw=true)

---

## Agora vamos analisar os generos

Vamos calcular a media de avaliações para cada genero 

```python
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)
```
![image.png](https://github.com/igorrzinho/Analise_dados/blob/main/bestselling-books/img/image%205.png?raw=true)

# 6º parte: exportando as informações

vamos exportar as informações que conseguimos

primeiro uma planilha de autores mais vedidos

```python
author_counts.head(10).to_csv("top_authors.csv")
```

agora uma de avaliação media por genero

```python
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
```

esses arquivos serão salvos na pasta onde esta o `main.py`
