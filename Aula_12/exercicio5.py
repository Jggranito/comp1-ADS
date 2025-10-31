tuplaNumeros = (1, 2, 6, 3, 5)

print(f'Primeiro numero: {tuplaNumeros[0]}\nUltimo numero: {tuplaNumeros[4]}')
print(f'Três primeiros numeros: {tuplaNumeros[:3]}')

numero = int(input('Digite um numero para verificar se está na tupla: '))

if numero in tuplaNumeros:
    print(f'O numero {numero} esta na lista')
else:
    print(f'O numero {numero} não esta na lista')