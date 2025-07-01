#Crie um programa  que receba o peso (kg)e a altura (m) de uma pessoa e calcule o IMC.
#Classifique o resultado de acordo com a faixa:
#Abaixo do peso (< 18.5)
#Peso normal (18.5 a 24.9)
#Sobrepeso (25 a 29.9)
#Obesidade (>= 30)


peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

   
if altura <= 0:
        print("Altura inválida. A altura deve ser maior que zero.")
else:
       
        imc = peso / (altura ** 2)

        print(f"Seu IMC é: {imc:.2f}")

       
        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif imc >= 18.5 and imc <= 24.9:
            print("Classificação: Peso normal")
        elif imc >= 25 and imc <= 29.9:
            print("Classificação: Sobrepeso")
        else: # imc >= 30
            print("Classificação: Obesidade")

