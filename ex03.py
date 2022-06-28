#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 3. Programa que verifica se é par ou ímpar e imprima a     
# mensagem respectiva.                                       

# Entrada de dados

valor = int(input("informe um valor: ")) # Solicita um valor inteiro do usuário

# Processamento de dados

if (valor % 2 == 0): # Se o valor for par, executará a identação
  print(f"{valor} é par") # Imprime a mensagem informando que o valor é par

else: # Se o valor for impar, executará a identação
  print(f"{valor} é impar") # Imprime a mensagem informando que o valor é impar

# Saída de dados

print("fim do programa") # Informa ao usuário que o programa terminou
