#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".

senha = input("Digite sua senha: ")

if len(senha) >= 8:
    print("Senha válida")
else:
    print("Senha muito curta")