listaDeCores = ['azul', 'amarelo', 'laranja', 'roxo', 'verde']

print(f'Lista de cores: {listaDeCores}')

removeCor = input('Digite uma cor da lista para ser removida: ')

listaDeCores.remove(removeCor.lower())

print(f'Lista de cores atualizada: {listaDeCores}')