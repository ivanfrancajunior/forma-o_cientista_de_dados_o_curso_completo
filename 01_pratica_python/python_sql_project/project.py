'''
Temos em mãos um arquivo com dados de pacientes que desenvolveram ou não diabetes. Precisamos gerar uma amostra de dados com os pacientes com mais de 50 anos e para
cada um deles indicar em uma nova coluna se o paciente está normal (índice de massa corpórea menor que 30) ou obeso (índice de massa corpórea maior ou igual a 30).

Então devemos gerar um novo arquivo CSV e encaminhar para o Cientista de Dados.

Vamos resolver esse problema com Banco de Dados, Python e SQL. Os dados serão
inicialmente carregados com Linguagem Python. Faremos então uma cópia dos dados para um
banco de dados e usaremos Linguagem SQL para as transformações necessárias.

Por fim, copiaremos os dados transformados de volta para um dataframe do Pandas para salvar o resultado em formato CSV.

REF: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
'''
#%%
import pandas as pd
import sqlite3



df = pd.read_csv('diabetes.csv')
# %%
df.head(10)
df.shape

#%%
!pip install ipython-sql

#%%
conn = sqlite3.connect('project_database.db')

df.to_sql('diabetes', conn)

'''começamos conectando o banco de dados e fazendo algumas consultas básicas'''
#%%
%load_ext sql
%sql sqlite:///project_database.db
#%%
%%sql
SELECT * FROM diabetes Limit 10

# %%
%%sql
SELECT Age,Glucose,Outcome FROM diabetes WHERE Glucose > 190

'''depois disso consultamos as colunas do dataframe original e criamos a tabela de pacientes a partir das colunas retornadas'''
# %%
df.columns
# %%
%%sql
CREATE TABLE pacientes (
 Pregnances INT, Glucose INT, BloodPressure INT, SkinThickness INT, Insulin INT, BMI FLOAT(8,2), DiabetesPedigreeFunction FLOAT(8,2), Age INT, Outcome INT
)

'''agora na nova tabela vamo inserir apenas os pacientes com mais de 50 anos via sql'''
# %%
%%sql
SELECT * FROM pacientes
# %%
%%sql
INSERT INTO pacientes (
 Pregnances, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome
)
SELECT Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome FROM diabetes WHERE Age > 50
# %%
'''Feita a inserção de dados, vamos verificar se os dados foram inseridos corretamente'''
%%sql
SELECT * FROM pacientes


'''Agora vamos adicionar uma coluna para indicar se o paciente é normal ou obeso caso o BMI for maior ou igual a 30 este paciente é considerado obeso caso contrario o paciente é considerado normal'''
# %%
%%sql
ALTER TABLE pacientes ADD COLUMN 'profile' VARCHAR (15)

# %%
%%sql
UPDATE pacientes SET profile = 'obeso' WHERE BMI >= 30
# %%
%%sql
UPDATE pacientes SET profile = 'normal' WHERE BMI < 30

# %%
'''verificamos novamente se os dados foram inseridos corretamente'''
%%sql
SELECT * FROM pacientes

# %%
'''Criamos uma variavel query para armazenar a consulta e utilizaremos ela para gerar um novo dataframe.

* Primeiro criamos um cursor com o resultado de query;

* Depois a partir da linha 1, pegamos o nome das colunas e criamos uma lista com os nomes armazenamos em outra variavel chamada cols;

* Agora criaremos um novo dataframe a partir do resultado da query onde cols será o nome das colunas e os dados serão os valores da query.

* Por fim salvaremos o resultado no arquivo dataset/diabetes_profile.csv
'''
query = conn.execute("SELECT * FROM pacientes")
print(query)
# %%
cols = [column[0] for column in query.description]
cols
# %%
result = pd.DataFrame.from_records(query.fetchall(), columns=cols)
# %%
result.head(10)
# %%
result.shape
# %%
result.to_csv('dataset/diabetes_profile.csv', index=False)
# %%
