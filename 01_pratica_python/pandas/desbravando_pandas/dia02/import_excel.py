#%%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")

# %%
df.shape

# %%
df.columns.tolist()

# %%
df.head()
# %%
df.tail()
# %%
cols = ['UUID', 'Points', 'IdCustomer', 'DtTransaction']

df = df[cols]
# %%
df
# %%
df.info(memory_usage='deep')
# %%
