n1 = int(input("Primeira nota: "))
n2 = int(input("Segunda nota: "))
n3 = int(input("Terceira nota: "))
m = (n1 + n2 + n3) / 3
f1 = int(input("Número de faltas: "))



if f1 >= 10:
    print("Reprovado por faltas")

elif f1 <= 10 and m >= 7: 
    print("Aprovado")

elif f1 <= 10 and m >= 5: 
    print("Recuperação")
    
else:
    print("Reprovado")

print(f"Sua média foi: {m}")