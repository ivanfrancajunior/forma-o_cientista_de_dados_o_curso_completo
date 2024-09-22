#%%
import pandas as pd
# %%
df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers.head()
# %%
df_customers.shape
# %%
df_customers.columns

# %%
df_customers.info(memory_usage="deep")
# %%
df_customers['Points'].describe()
# %%
''' Ao utilizar uma condição lógica no pandas fazendo comparações em uma serie com algum valor e ela retornar um valor booleano, podemos passar a condição para o pandas para filtrar o dataframe'''

condicao = df_customers['Points']  > 1000
# %%
df_customers[condicao]
# %%
'''achando o usuário com maior numero de pontos'''
maximo = df_customers['Points'] == df_customers['Points'].max()
# %%
user_com_mais_pontos = df_customers[maximo]

user_com_mais_pontos['Name'].iloc[0]
# %%
''' Filtrando os usuários entre 1000 e 2000 pontos utilizando AND (&) '''

entre_1000_e_2000 = (df_customers['Points'] >= 1000) & (df_customers['Points'] <=2000)

entre_1000_e_2000

# %%
''' Adicionando uma nova referencia ao dataframe original utilizando o .copy()'''

df_1000_2000 = df_customers[entre_1000_e_2000].copy()

df_1000_2000['Points'] = df_1000_2000['Points'] + 1000

df_1000_2000

#%%
#%%
''' Retornando o dataframe com as colunas em ordem alfabetica:
* pegamos as colunas e passamos para uma lista

* os colunas estando em lista, podemos utilizar o .sort() para ordernanar a lista

* com as colunas ordenadas, passamos para o dataframe esta nova condição e reatribuimos  a
ele a condição desta forma a condição inicial passa a ser a ordenada.

'''
#%%
colunas = df_customers.columns.tolist()

#%%
colunas.sort()
colunas

# %%
df_customers = df_customers[colunas]
df_customers
# %%
''' Renomeando as colunas: Ao utilizar o .rename() podemos renomear as colunas do dataframe

O dataframe original permanece intacto, e o novo dataframe e criado com as colunas renomeadas
'''
df_customers = df_customers.rename(columns={'Name':'Nome', 'Points':'Pontos', 'UUID': 'Id'})
#%%
df_customers
# %%
