# real = float(input("Diigte o valor em real a ser convertido: "))
# dolar = real/5.29
# euro = real/6.18
# print("R${:.2f} valem UU${:.2f} dolares, €{:.2f} Euros".format(real, dolar, euro))

# A = 30
# B = 20
# C = A + B
# print (C)
# B = 10
# print (B, C)
# C = A + B
# print (A, B, C)

# a = 10
# b = 30 
# print(a, b + 10)
# b = a
# a = b - 5
# print(a, b)

# print('Entrada - Rock & Code Party')

# ano_atual = 2021
# ano_nasc = int(input())

# idade = ano_atual - ano_nasc

# if idade >= 18:
#     print('Entrada permitida.')
# elif idade > 14:
#     print('Entrada permitida desde que acompanhado(a).')
# else:
#     # print('Entrada proibida.')

# T = 1
# M = 5
# C = 10

# while T < M:
#     C = C * (1 + T)
#     T = T + 1

# print(C)

# T = 1
# M = 5
# C = 10
# C = C * (1 + T)

# while T < M:
#     T = T + 1
        
# print(C)
# T = 1
# M = 5
# C = 10
# C = C * (1 + T)

# for T in range(M):
#     C = C * (1 + T)
        
# print(C)

from random import randint

n = 7
a = 0

for i in range(n):
    num_aleat = randint(0, 50)
    if num_aleat > a and num_aleat <= 40:
        a = num_aleat

print(a)