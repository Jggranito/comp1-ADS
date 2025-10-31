#Agora, a nossa pizzaria está cobrando uma taxa fixa de R$5 por entrega, além de R$1 por km até 5km, e R$2 por km até 10km. Mais ainda não entregamos com a distância superior a 10km.

#Pegando como base essas possibilidaes, faça um programa que responda as seguintes perguntas:
# - Quanto Joana irá pagar de frete, sendo que mora a 8km da pizzaria.
# - Quanto Guilherme irá pagar de frete, sendo que mora a 3km da pizzaria.
# - Quanto Rafael irá pagar de frete, sendo que mora a 11km da pizzaria.

taxaFixa = 5

while True:
    try:
        distancia = int(input("Digite somente com números quantos km de distância você se encontra de nós:   "))
        break
    except ValueError:
        print("❌ Valor de entrada inválido! Digite apenas números inteiros!")

if distancia > 0 and distancia <= 5:
    print("Taxa de entrega: ", (taxaFixa + (1*distancia)))
elif distancia > 5 and distancia <= 10:
    print("Taxa de entrega: ", (taxaFixa + (2*distancia)))
elif distancia > 10:
    print("Não realizamos entregas acima de 10km 🙁")
else:
    print("❌ Valor de entrada inválido!")