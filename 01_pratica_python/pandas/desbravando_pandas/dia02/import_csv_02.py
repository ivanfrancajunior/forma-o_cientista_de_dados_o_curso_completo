# %%
import pandas as pd

df = pd.read_csv('../data/products.csv', sep=';',  names=['id','product','description'])


# %%
df.columns

# %%
df = df.rename(columns={"id":"ID", "product":"Produto", "Description":"Descricao"})
# %%
df
# %%
