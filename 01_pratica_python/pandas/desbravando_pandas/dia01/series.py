#%%
# !pip install pandas

# %%
import pandas as pd

idades = [50, 30, 27, 12 ]
idades
# %%
media = sum(idades)/len(idades)
media

# %%

total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) -1)
variancia

# %%
''' iniciando uma serie com python'''

series_idades = pd.Series(idades, name='idades')
series_idades
# %%
series_idades.mean()

# %%
series_idades.var()

# %%
series_idades.median()

# %%
'''retorna um resumo dos dados da serie'''
series_idades.describe()
# %%
series_idades.shape

# %%
''' alterando indices da serie '''
series_idades.index = ['j', 'o', 't','a']

# %%
series_idades
# %%
''' acessando elementos pelo indice '''
series_idades['a']
# %%
''' acessando elementos pelo indice usando loc'''
series_idades.loc['o']
# %%
''' acessando elementos pela posicao '''
series_idades.iloc[3]
# %%
''' acessando intervalo de elementos pela posicao '''
series_idades.iloc[0:3]

# %%
series_idades
# %%
