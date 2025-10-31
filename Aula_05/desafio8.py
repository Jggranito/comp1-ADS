print("""
       =======================================
          Bem vindo ao Banco Digital, onde o
         seu endividamento e a nossa alegria!
       =======================================
""")

saldoAtual = float(input("Informe o saldo atual da sua conta: "))
saque = float(input("Informe o valor do saque: "))

if saldoAtual < saque:
    print("Saldo insuficiente! Saque negado 😊")
else:
    print("Saque aprovado 🙁. Novo saldo -> R$%.2f" % (saldoAtual - saque)) 