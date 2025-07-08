#Peça a idade do usuário e diga se ele pode se cadastrar em um site:

#Permitido: 13 anos ou mais

idade = int(input("Por favor, digite sua idade: "))

if idade >= 13:
    print("Você pode se cadastrar no site. Bem-vindo(a)!")
else:
    print("Desculpe, você não pode se cadastrar no site ainda. A idade mínima é de 13 anos.")