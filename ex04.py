#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 4. Elabore um algoritmo que calcule e imprima o salário    
# reajustado de um funcionário de acordo com a seguinte regra
# Salários até R$ 300,00, reajuste de 50%;                   
# Salários maiores que R$ 300,00, reajuste de 30%.           

# Entrada de dados

salario = float(input("informe o salário: ")) # Solicita o salário do usuário

# Processamento e saída de dados

if (salario <= 300): # Se o salario for menor ou igual a 300 executará a identação
  salario = salario + (salario * 0.5) # Aplica o reajuste de 50%
  print(f"O salário reajustado é de R${salario:.2f}") # Imprime o salário reajustado

else: # Qualquer valor acima de 300
  salario = salario + (salario * 0.3) # Aplica o reajuste de 30%
  print(f"O salário reajustado é de R${salario:.2f}") # Imprime o salário reajustado

print("fim do programa") # Informa ao usuário que o programa terminou
