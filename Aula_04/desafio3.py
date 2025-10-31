# -*- coding: utf-8 -*-
# Crie um programa que calcula o **valor final de um pedido**, aplicando um desconto específico caso a compra seja feita em um dia de promoção.

# - Terça-feira: Pedidos acima de R$ 40 recebem uma sobremesa grátis (exiba uma mensagem).
# - Quarta-feira: Todas as pizzas têm 15% de desconto.
# - Sábado e Domingo: Pedidos acima de R$ 100 têm a taxa de entrega grátis (considere a taxa fixa de R$ 5 que seria cobrada).
# - Para os outros dias, não há promoção.

TAXA = 5 # Constante FAKE

def pedidos():
    pedidosClientes = {
        'Mariana': {
        'valorDoPedido': 80,
        'diaDaSemana': 'terça',
        'distancia': 0
        },
        'Guilherme': {
        'valorDoPedido': 50 ,
        'diaDaSemana': 'quarta',
        'distancia': 0
        },
        'Rafael': {
        'valorDoPedido': 120,
        'diaDaSemana': 'domingo',
        'distancia': 4
        }
    }
    return pedidosClientes
    
meusPedidos = pedidos()
taxaEntrega = 0

for cliente, dados in meusPedidos.items():
    valorPedido = dados['valorDoPedido']
    diaSemana = dados["diaDaSemana"]

    print(f' Dia: {diaSemana}, Valor do Pedido: R${valorPedido:.2f}')
    if diaSemana == "terça" and valorPedido > 40:
        print("  Promoção aplicada. Sobremesa grátis.")
        if dados['distancia'] >= 0 and dados['distancia'] <= 5:
            taxaEntrega + (TAXA + (1 * dados['distancia']))
        elif dados['distancia'] > 5 and dados['distancia'] <= 10:
            taxaEntrega = (TAXA + (2 * dados['distancia']))
        elif dados['distancia']:
            print("Não realizamos entregas acima de 10km ")
        valorFinal = valorPedido + taxaEntrega
        
    elif diaSemana == "quarta":
        if dados['distancia'] >= 0 and dados['distancia'] <= 5:
            taxaEntrega =  (TAXA + (1 * dados['distancia']))
        elif dados['distancia'] > 5 and dados['distancia'] <= 10:
            taxaEntrega = (TAXA + (2 * dados['distancia']))
        elif dados['distancia']:
            print("Não realizamos entregas acima de 10km ")
        valorFinal = (valorPedido + taxaEntrega) * 0.85 # Variável local
        print("  Promoção aplicada: 15% de desconto!")
        
    elif diaSemana == "sabado" or diaSemana == "domingo" and valorPedido > 100:
        taxaEntrega = 0  # Variável local
        valorFinal = valorPedido + taxaEntrega
    else:
        print("  Sem promoção!")
    
    print(f"""
        ================================
         Pedido realizado com sucesso!
         
         Taxa de entrega: R${taxaEntrega:.2f}
         Valor total: R${valorFinal}
    """)