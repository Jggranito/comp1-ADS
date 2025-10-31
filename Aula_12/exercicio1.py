nomes = []

while True:
    nome = input("Digite o nome (ou sair): ")
    
    if nome.lower() == 'sair':
        break
    
    nomes.append(nome)
    
print(f"Nomes cadastrados: {nomes}")