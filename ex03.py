
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# par ou ímpar e imprima a mensagem respectiva.

valor = int(input("informe um valor: ")) # entrada de dados

# processamento
if (valor % 2 == 0): # se o valor for par
  print(f"{valor} é par")
else: # se o valor for impar
  print(f"{valor} é impar")

