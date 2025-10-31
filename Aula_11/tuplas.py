tuplaDeNumeros = (1, 2, 3)
tuplaDadosCidade = ("Rio de Janeira", "RJ", True, 21, 500.00)

#Acesso por slicing
tuplaDadosFatiados = tuplaDadosCidade[1:4]
print(tuplaDadosFatiados)

# Acesso poríndice
print(tuplaDeNumeros) # Exibe a tupla completa
print(tuplaDadosCidade[3]) # Exibe o 21, que é o item no terceiro índice.
print(tuplaDadosCidade[-1]) # Exibe o 500.00, que é o último índice.