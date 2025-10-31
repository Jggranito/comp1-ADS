#Crie um desafio que calcule o valor do frete com base na distânia:
#Até 5km, R$5
#De 6km até 10km, R$10
#Acima de 10km, exibir que a entrega não é feita 

while True:
    try:
        distancia = int(input("Digite somente com números quantos km de distância você se encontra de nós:   "))
        break
    except ValueError:
        print("❌ Valor de entrada inválido! Digite apenas números inteiros!")

if distancia > 0 and distancia <= 5:
    taxa = 5
    print("Taxa de entrega: ", taxa)
elif distancia > 5 and distancia <= 10:
    taxa = 10
    print("Taxa de entrega: ",  taxa)
elif distancia > 10:
    print("Não realizamos entregas acima de 10km 🙁")
else:
    print("❌ Valor de entrada inválido!")