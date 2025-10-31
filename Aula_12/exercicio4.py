listaNumero = []

for i in range(5):
    numero = input(f'Digite o {i}° numero da lista: ')
    listaNumero.append(numero)
    
print(f'Lista: {listaNumero}')

listaNumero.sort()

print(f'Lista ordenada: {listaNumero}')

listaNumero.reverse()

print(f'Lista ordenada invertida: {listaNumero}')