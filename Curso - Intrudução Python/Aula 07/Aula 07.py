# def big_mac():
#     nome = input("Qual o seu nome? ")
#     sanduiche = (input(f"Qual o seu sanduiche, {nome}? "))
#     bebida = (input(f"qual refrigerante?"))

#     print(f"{nome} retire o seu {sanduiche} e {bebida}, no balcão")


# print('inicio')
# big_mac()   
# print('fim')

# def big_mac():
#     print('sanduiche big mac')

# print('inicio')
# big_mac()
# print('fim')

def fazer_big_mac(nome):
    print(f'sanduiche big mac {nome}')

# fazer_big_mac('Ramon')
# fazer_big_mac('Cita')
# fazer_big_mac('Louro')

def fazer_batata(tamanho):
    print(f'Batata {tamanho}')

def preparar_refrigerante(tipo,tamanho):
    print(f'{tipo} {tamanho}')

# fazer_big_mac('Ramon')
# fazer_batata('Grande')
# preparar_refrigerante('Pepsi','Grande')

def fazer_combo_big_mac(nome,tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri,tamanho_refri)

# fazer_combo_big_mac('Ramon','Média','Pepsi','Grande')

def som_num(num1,num2):
    return num1 + num2

# resultado = som_num(15,20)
# print(resultado)

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

resultado = maior_num([2,88,644,-4854,547,548,-5026])
print(resultado)
