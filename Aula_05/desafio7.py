valorCamiseta = 50

print("""
       ======================================
            camisetas por R$ 50,00 cada
            
            *Acima de 3 camisetas 20% 
                    de desconto
       ======================================
""")

qntCamisetas = int(input("Quantas camisetas voce deseja comprar? "))

if qntCamisetas > 2:
    print("Desconto aplicado! Valor final -> R$%.2f" % ((qntCamisetas * valorCamiseta) * 0.8))
else:
    print("Valor final -> R$%.2f" % (qntCamisetas * valorCamiseta))