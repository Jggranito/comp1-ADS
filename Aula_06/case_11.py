ARROZ = 20.00
FEIJAO = 10.00
OLEO = 8.00

print("""
            ======================================
                Bem vindo mercado Compra Fácil
                      
                    Preços:
                     Arroz  -> R$ 20,00
                     Feijão -> R$ 10,00
                     Óleo   -> R$  8,00
            ======================================
""")

qntArroz = int(input("Informe quantas unidades de arroz você deseja: "))
qntFeijao = int(input("Informe quantas unidades de feijão você deseja: "))
qntOleo = int(input("Informe quantas unidades de óleo você deseja: "))

valorTotal = (qntArroz * ARROZ) + (qntFeijao * FEIJAO) + (qntOleo * OLEO)

if valorTotal > 100:
    valorTotal = valorTotal * 0.85
    
print("Total de itens pedidos: ", (qntArroz + qntFeijao + qntOleo), "\nValor total: R$ %0.2f" % valorTotal)