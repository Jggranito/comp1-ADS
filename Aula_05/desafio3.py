valorGasolina = 5.5
valorEtanol = 4

print("""
       ==================================
             Bem vindo ao Abastece Bem
      
          Valor dos combustiveis:
          Gasolina -> R$ 5,50/litro
          Etanol   -> R$ 4,00/litro
          
       ===================================
""")

combustivel = int(input("Qual combustivel deseja (1 para Gasolina; 2 para Etanol): "))
qntLitros = float(input("Quantos litros deseja abastecer: "))

if combustivel == 1:
    print("Valor a pagar: R$%.2f" % (valorGasolina * qntLitros))
elif combustivel == 2:
    if qntLitros > 20:
        print("Valor a pagar: R$%.2f" % ((valorEtanol * qntLitros) * 0.95))
    else:
        print("Valor a pagar: R$%.2f" % (valorEtanol * qntLitros))