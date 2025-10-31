while True:
    senha = input("Digite sua senha: ")
    if len(senha) < 8:
        print("Sua senha deve ter no mínimo 8 caracteres.")
    else:
        break