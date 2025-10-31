from random import randint as rd

numero_aletaorio = rd(1, 20)
tentativas = 0

print("Tente adivinhar o número sorteado\n\n")

while True:
    palpite = int(input("Digite seu palpite: "))
    difernca = abs(numero_aletaorio - palpite)
    
    if palpite == numero_aletaorio:
        print(f"Parabéns, você acertou!! Total de tentativas {tentativas}")
        break
    else:
        tentativas += 1
        if difernca <= 3:
            print("Quase lá! Você chegou muito perto 😲")
        elif difernca <= 6:
            print("Quase! Você está chegando lá 👀")
        else:
            print("Muito longe! Tente novamente. 🙁")