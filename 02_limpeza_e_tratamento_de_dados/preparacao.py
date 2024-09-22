#%%
import pandas as pd
import seaborn as srn
import statistics as st

dataset = pd.read_csv('Churn.csv', sep=';')


# %%
''' #1: tabalas com dado sem significado(tabelas em que o titulo das colunas não possuem um significado) '''
dataset.head(10)
# %%
dataset.shape

# %%
dataset.columns = ['id', 'score', 'estado', 'genero', 'idade','patrimonio', 'saldo', 'produtos', 'possui_credito', 'membro_ativos', 'salario', 'saiu' ]
# %%
dataset.head(10)

# %%
# analise exploratória - estados
groupe_by_state = dataset.groupby('estado').size()

# groupe_by_state.plot.bar(color='orange')

''' #2: Depois da analise se constata que 2 estados não existes RP e TD, outra problematica é o estado de SP uma vez que os dados são referentes a estados do Sul saindo do dominio e caso eles sejam mantidos podem ocasionar erros no modelo.

Como solução vamos substituir usando a regra da MODA para substituir os dados 'errados' e a moda neste caso é o RS'''

groupe_by_gender = dataset.groupby('genero').size()
'''
dados de fontes diferentes: uma mesma informação pode chegar de formas diferentes.
No caso do genero temos F, Fem, Feminino, M e Masculino como dados obtidos e estes dados não podem ser alterados pois possuem significado porém precisam ser tratados para que fiquem padronizados.
'''

# groupe_by_gender.plot.bar(color=['#ff69b4','green'])

# %%
dataset['score'].describe()

# %%
