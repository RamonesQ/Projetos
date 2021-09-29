# tenho_sede = True

# if tenho_sede:
#     print('beber agua')
# print('Vida que segue')

# esta_frio = True

# if esta_frio:
#     print('Vestir um casaco')
# else:
#     print('Vestir uma camiseta')

# tenho_sede = False
# tenho_fome = False
# estou_em_dieta = False

# if tenho_sede or tenho_fome:
#     print('Vou na cozinha')
# else:
#     print('Ficar vendo netflix')

# if tenho_sede and tenho_fome:
#     print('Fazer sanduiche e pegar um refri')
# else:
#     print('não tenho fome ou não tenho sede')

# if tenho_sede and tenho_fome:
#     print('Fazer sanduiche e pegar um refri')
# elif tenho_sede and not (tenho_fome):
#     if estou_em_dieta:
#         print('beber agua')
#     else:
#         print('Tomar uma coquinha')
# elif not(tenho_sede) and tenho_fome:
#     print('Fazer um sanduiche')
# else:
#     print('ficar vendo netflix')

from typing import overload


num1 = int(input("Primeira nota: "))
num2 = int(input("Segunda nota: "))

if num1 == num2:
    print('num1 é igual num2')
elif num1 != num2:
    print('num1 é difierente de num2')

# if num1 <= num2:
#     print('num1 é menor que num2')
# elif num1 >= num2:
#     print('num1 é maior que num2')

# Operadores lógicos

# or = ou 
# and = e
# not() = negação

# Operadores de comparação

# == - igaul
# != - diferente
# > - maior que
# < - menor que
# >= - maior ou igual
# <= - menor ou igaul
