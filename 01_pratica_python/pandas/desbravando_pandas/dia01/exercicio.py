'''
Converta a seguinte lista de dados para uma Series Pandas e obtenha:
Média
Desvio Padrão
Máximo Valor

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]

'''
# %%
import pandas as pd

# %%
data = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]

serie = pd.Series(data, name="numbers")
serie

# %%
serie_description = serie.describe()
serie_description
# %%
mean = serie_description["mean"]
mean
# %%
std = serie_description["std"]
std
# %%
max = serie_description["max"]
max

'''
Converta o seguinte dicionário para DataFrame e obtenha:
Sumário de cada coluna
Média da coluna idade
Último nome da coluna nome

'''
#%%
dados = { 'nome':  ['Téo', 'Nah', 'Lah'],
          'idade': [31, 32, 14]}

df = pd.DataFrame(dados)
# %%
nomes = df['nome'].describe()
nomes

#%%
idades = df['idade'].describe()
idades

#%%
media_idades = idades['mean']
media_idades.round(2)
# %%
ultimo_nome = df['nome'].iloc[-1]
ultimo_nome
# %%
