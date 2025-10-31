idade = int(input("Informe a sua idade: "))

if idade < 12:
    print("Voce e uma crianca")
elif idade >= 12 and idade <= 17:
    print("Voce e adolescente")
elif idade >= 18 and idade <= 59:
    print("Voce e adulto")
else:
    print("Voce e idoso")