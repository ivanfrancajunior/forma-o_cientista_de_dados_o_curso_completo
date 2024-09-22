#%%
# !pip install ipython-sql
# %%

''' Neste exemplo criaremos uma nova coneção com banco de dados e a partir de um dataframe criado, vamos inserir-lo em uma tabela sqlite utilizando a conexão.

Para isso vamos utilizar as libs pandas para criar um dataframe e ipython-sql para criar e utilizar a conexão com o sqlite e também executar queries em sql. '''

import pandas as pd
import sqlite3

sample = pd.DataFrame(
    {'nome':['Siri', 'Alexa', 'Cortana'],
     'idade':[28,47,18],
     'cargo':['Cientista de dados', 'Analista de dados', 'estagiário']}
)

sample.head()
# %%
conn = sqlite3.connect('sample_database.db')
# %%
# criando uma tabela e inserindo os dados
sample.to_sql('funcionarios', conn)

#%%
# carregando extenção sql via ipython-sql e indicando o banco de dados a ser utilizado

# Para usar queries em sql, agora temos que iniciar com o comando %%sql pra iniciar o ipython-sql

%load_ext sql
%sql sqlite:///sample_database.db

# %%
%%sql
SELECT * FROM funcionarios

# %%
%%sql
SELECT count (*) FROM funcionarios
# %%

%%sql
SELECT avg(idade) as 'media_idade' FROM funcionarios
# %%
