# FOR -> É uma das estruturas de repetição mais utilizadas e poderosas da linguagem. Ele serve para iterar sobre os itens de qualquer sequência (lista, tupla, string).
# for item in sequencia:
    #Bloco de código a ser executado
    #para cada 'item' da 'sequencia'.
    
lista_de_frutas = ["Maça", "Banana", "Morango", "Uva"]
for fruta in lista_de_frutas:
    print(f"Comprei {fruta}")
    
# => range() - Utilizado para quando precisamos executar um bloco de código um número específico de vezes
# range(5) - Toda vez que a função range é utilizada, o número passado será exclusivo(não será executado)

print("Contanto até 4: ")
for numero in range(5):
    print(numero)

# Imprimir os números pares de 2 à 10
print("Números pares de 2 a 10")
for i in range(2, 11, 2):
    print(f"Numero par: {i}")