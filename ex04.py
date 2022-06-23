#
# Elabore um algoritmo que calcule e imprima o salário reajustado de um funcionário
# de acordo com a seguinte regra:
# Salários até R$ 300,00, reajuste de 50%;
# Salários maiores que R$ 300,00, reajuste de 30%.

# entrada de dados
salario = float(input("informe o salário: "))

# processamento e saida de dados
if (salario <= 300): # se o salario for menor ou igual a 300
  salario = salario + (salario * 0.5) # reajuste de 50%
  print(f"O salário reajustado é de R${salario:.2f}")
else: # se o salario for maior que 300
  salario = salario + (salario * 0.3) # reajuste de 30%
  print(f"O salário reajustado é de R${salario:.2f}")

print("Fim do programa")

