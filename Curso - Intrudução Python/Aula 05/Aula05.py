# Aula 05 Input de usuario e calculadora

# Função Input("") Permite recdeber uma informação externa ao script
# Função Int - Identifica como um numero inteiro
# Função F"texto"{} permite adicionar informações de outra string 

#Input de usuario

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade, {nome}? "))
nascimento = 2021 - idade
print(f"{nome} você nasceu em {nascimento}")

#Calculadora Simples

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
resultado = num1 + num2

print(f"O Resultado é: {resultado}")