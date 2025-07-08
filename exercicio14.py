#Loja oferece os seguintes descontos:

#Compras acima de R$ 500,00 têm 10%
#Acima de R$ 300,00 têm 5%
#Menor ou igual a R$ 300,00 não têm desconto


valor_compra = float(input("Digite o valor total da compra em R$: "))

   
if valor_compra > 500:
        desconto = 0.10 
        print("Você ganhou 10% de desconto!")
elif valor_compra > 300: 
        desconto = 0.05
        print("Você ganhou 5% de desconto!")
else: 
        print("Para compras de R$ 300,00 ou menos, não há desconto.")

valor_final = valor_compra * (1 - desconto)
print(f"Valor original da compra: R$ {valor_compra:.2f}")
  

