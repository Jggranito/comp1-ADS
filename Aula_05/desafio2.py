valorIngresso = 20.00

print("""
       ==================================
             Bem vindo ao CineMais
      
          Ingressos:
          Menor que 12 anos  -> R$ 10,00
          60 anos ou mais    -> R$ 12,00
          Inteira            -> R$ 20,00
          
       ===================================
""")

idade = int(input("Digite sua idade: "))

if idade > 12 and idade < 60:
    print("Valor do seu ingresso: %.2f" % valorIngresso)
elif idade < 12:
    print("Valor do seu ingresso: %.2f" % (valorIngresso * 0.5))
else:
    print("Valor do seu ingresso: %.2f" % (valorIngresso * 0.6))