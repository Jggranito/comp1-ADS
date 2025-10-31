print("""
       ======================================
               Calculadora de IMC
       ======================================
""")

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso / (altura * altura)

print("Seu imc é: %.2f" % imc)

if imc < 18.5:
    print("Voce esta abaixo do peso ideal")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Voce esta com sobrepeso")
elif imc >= 30:
    print("Voce esta com obesidade")