print("""
       ===================================
            Conversor de temperatura
       ===================================
""")

tempCelsius = float(input("Informe a temperatura em graus Celsius: "))
opcaoConversao = int(input("""
    Escolha a opcao da unidade para conversao:
                        
    1 - Fahrenheit (F)
    2 - Kelvin (k) 
"""))

if opcaoConversao == 1:
    print("Resultado da conversao: %.2f" % tempCelsius, "° Celsius = %.2f" % ((tempCelsius * (9/5)) + 32), "° Fahrenheit")
elif opcaoConversao == 2:
    print("Resultado da conversao: %.2f" % tempCelsius, "° Celsius = %.2f" % ((tempCelsius + 273.15)), "° Kelvin")
else:
    print("Opcao invalida.")