# O Numpy é uma lib para trabalhar com matrizes, mais especialmente matrizes unidimensionais.

#%%
import numpy as np

# criando matrizes unidimensionais especificando o tipo
mt= np.array([12, 13, 14, 15, 16, 17],dtype=float)


mt2=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],dtype=int)

# print(mt,mt2, sep='\n')
# print(type(mt), type(mt2), sep='\n')


# fazendo conversão de tipos (astype method)
mt_new=mt2.astype(float)
# print(mt_new, sep='\n')



#criando matrizes bidimensionais
mt3=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(mt3)

# criando arrays vazios tipificados
print('*************************')
empty = np.empty([3,2], dtype=int)
print(empty)
print('*************************')


# criando arrays com zeros
zeros = np.zeros([3,2], dtype=int)
print(zeros)
print('*************************')


# criando arrays com 1
ones = np.ones([3,2], dtype=int)
print(ones)
print('*************************')

#criando matriz quadrada com diagonal principal com valores 1 e os demais valores 0

diagonal = np.eye(5)
print(diagonal)

# criando numeros aleatórios
random = np.random.random((10))
print(random)


# criando uma sequência de valores com distribuição normal e numeros negativos

randn = np.random.randn(10)
print(randn)

# criando matriz aleatória
mat_rand = np.random.random((5,5), dtype=int)
print(mat_rand)
# %%

#gerando numeros aleatóerios entre usando semente
# semente é uma forma de garantir  que os valores gerados sejam os mesmos ao longo do tempo

gnr_w_seed = np.random.default_rng(5)
numbers = gnr_w_seed.random(10)
print(numbers)
# %%
