despesa = ["arroz", "feijão", "óleo"]

item = input('Digite o item que você quer verificar: ').lower()

if item in despesa:
    print(f"{item} já existe na dispensa")
else:
    print(f"O item {item} precisa ser comprado.")