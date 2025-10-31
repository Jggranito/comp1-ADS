print("""
       ======================================
               Calculadora Simples
      
         Digite o numero da opracao desejada
          
        1 = Soma
        2 = Subtracao
        3 = Multiplicacao
        4 = Divisao
       ======================================
""")

operacao = int(input())

num1 = float(input("Primeiro numero: "))
num2 = float(input("Segundo numero: "))

if operacao == 1:
    print("Soma -> %.2f" % num1, "+ %.2f" % num2, "= %.2f" % (num1 + num2))
elif operacao == 2:
    print("Subtracao -> %.2f" % num1, "- %.2f" % num2, "= %.2f" % (num1 - num2))
elif operacao == 3:
    print("Multiplicacao -> %.2f" % num1, "* %.2f" % num2, "= %.2f" % (num1 * num2))
elif operacao == 4:
    print("Divisao -> %.2f" % num1, "/ %.2f" % num2, "= %.2f" % (num1 / num2))
else:
    print("Opcao inválida.")