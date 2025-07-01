
salario_atual_str = input("Digite o valor do salário atual: R$ ")
salario_atual = float(salario_atual)

if salario_atual <= 2000.00:
 percentual_reajuste = 0.15  # 15%
elif 2000.01 <= salario_atual <= 5000.00:
 percentual_reajuste = 0.10  # 10%
else:  # salario_atual > 5000.00
 percentual_reajuste = 0.05  # 5%

        