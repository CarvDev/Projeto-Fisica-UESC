# ESSE É UM ARQUIVO DE TESTE, ELE NÃO PERMANECERÁ NO PROJETO FINAL

import numpy as np

# arrays normais:

# declarando array unidimensional de inteiros:
a = np.array([1, 2, 3, 4, 5])

# imprimindo array completo:
print(a)

# imprimindo somente elemento da posição 3:
print(a[2])

# imprimindo elementos da posição 1 a 3
print(a[:3])

# imprimindo elementos após o 3:
print(a[3:])


# declarando e imprimindo array bidimensional de floats
b = np.array([[1.0, 2.1, 3.2, 4.5], [5.4, 6.3, 7.2, 8.6], [9.1, 10.2, 11.5, 12.6]])
print(b)

# imprimindo número de dimensôes dos arrays
print(a.ndim)
print(b.ndim)

# imprimindo número de elementos em cada dimensão do array:
print(a.shape)
print(b.shape)

# imprimindo o número total de elementos dos arrays:
print(a.size)
print(b.size)

# imprimindo o tipo de dados dos arrays:
print(a.dtype)
print(b.dtype)

print(end="\n\n") #pulando linhas para organizar

# outros arrays:

# criando um array vazio de 3 posições (economiza memória e é mais rápido):
c = np.empty(3) 
# imprimindo array vazio (saída esperada: lixo)
print(c)

# criando e imprimindo um array de 4 posições, em ordem crescente, começando do 0:
d = np.arange(4)
print(d)

# criando e imprimindo um array de que se inicia em 2 e é acrescido de 2 em 2, porém limitado a 9
e = np.arange(2, 9, 2)
print(e)

# criando e imprimindo array de 5 posições com valores espaçados igualmente, iniciando em 0 e terminando em 10
f = np.linspace(0, 10, num=5)
