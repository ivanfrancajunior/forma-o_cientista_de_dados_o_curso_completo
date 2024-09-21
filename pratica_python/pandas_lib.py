# pandas é a lib utilizada para trabalhar dados tabulares ou seja, dados em formato de tabela

# dataframes: dados em formato de tabela

#series: Uma unica coluna ou vetor de dados

#%%
import pandas as pd

#carregando dados
data = pd.read_csv('./Credit.csv')

#exibindo formato dos dados
#%%
# data.shape

# # exibindo resumo numerico dos dados
# data.describe()

# %%
#exibindo primeiras linhas
# data.head(5)

# %%
#últimos registros, com parâmetros
# data.tail(2)

#filtras por nome da coluna
# data[['duration']]

# filtrar linhas por indice
data.loc[1:3]

#filtrar linhas específicas
data.loc[[1,3]]

#filtro
data.loc[data['purpose'] == "radio/tv"]

#outra condição
# data.loc[data['credit_amount'] >  18000]

# retornando apenas colunas especificas
credit = data[['checking_status', 'duration']].loc[data['credit_amount'] > 15000]

print(credit)

# %%
