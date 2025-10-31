valorBala = 0.5
valorChocolate = 2

print("""
       =================================
             Bem vindo a Doce Sabor
      
          Cardapio:
          Bala      -> R$ 0,50
          Chocolate -> R$ 2,00
          
          *Compras acima de R$ 20,00
          recebem 10% de desconto
       ==================================
""")

compraBala = int(input(("Quantas balas voce deseja comprar? ")))
compraChocolate = int(input(("Quantos chocolates voce deseja comprar? ")))
valorTotal = (compraBala * valorBala) + (compraChocolate * valorChocolate)

if ( valorTotal > 20 ):
    valorTotal = valorTotal * 0.9
    print("Parabéns, voce ganhou um desconto de 10%!\n Valor total da compra: ", valorTotal)
else:
    print("Valor total da compra: %.2f" %valorTotal)