qntHora = float(input("Quantas horas o carro ficou no estacionamento? "))

if qntHora <= 1:
    valorAPagar = 5
elif qntHora <= 3:
    valorAPagar = 10
else:
    if qntHora < 4: 
        valorAPagar = 12.5
    else:
        valorAPagar = 10 + (2.5 * int(qntHora - 3))
        
print(valorAPagar)