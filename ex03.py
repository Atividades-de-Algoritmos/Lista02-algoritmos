#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 3. Programa que verifica se é par ou ímpar e imprima a     
# mensagem respectiva.                                       

# Entrada de dados

valor = int(input("informe um valor: ")) # Solicita um valor inteiro do usuário

# processamento de dados

if (valor % 2 == 0): # se o valor for par imprime a resposta pro usuário
  print(f"{valor} é par") # imprime a mensagem se o valor for par

else: # se o valor for impar imprime a resposta pro usuário
  print(f"{valor} é impar") # imprime a mensagem se o valor for impar

# saída de dados
print("fim do programa") # Informa ao usuário que o programa terminou
