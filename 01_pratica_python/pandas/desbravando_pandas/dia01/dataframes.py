'''dataframes são conjuntos de series, cada coluna do dataframe e um conjunto de series'''
# %%
import pandas as pd

data = {
    'nome':['Jota', 'Elaine', 'Ivan', 'Arthur', 'Hiane'],

    'idades':[30,55, 59,8,26 ],

    'sobrenomes':['da silva', 'da silva', 'da silva', 'da silva', 'da silva']
}
#%%
data
#%%
idade = data['idades'][0]
idade
# %%
sobrenome = data['sobrenomes'][0]
sobrenome
#%%
df = pd.DataFrame(data)
df
'''loc x iloc

usando .loc o resultado retornado é o valor do indice especificado já o .iloc retorna o valor na posição especificada
'''
# %%
df['idades'].iloc[0]

# %%
type(df['idades'])
# %%
df['nome']
# %%
''' selecionando uma linha também é uma serie onde os indices das series são os nomes das colunas'''

jota = df.iloc[0]
# %%
jota
# %%
arthur = df.iloc[3]
arthur
# %%
df.index
# %%
df.columns
# %%
''' Exibe informações sobre o dataframe com mais detalhes'''
df.info(memory_usage='deep')

# %%
'''Exibe uma serie onde o index é o nome da coluna e o valor é o tipo da coluna'''
df.dtypes
# %%
'''Aplica em todas as colunas numericas as estatisticas descritivas'''
df.describe()
# %%
df['peso'] = [80, 70, 60, 50, 40]


# %%
df.describe()
# %%
sumario = df.describe()
sumario['peso']['mean']

# %%
df[0:]

# %%
