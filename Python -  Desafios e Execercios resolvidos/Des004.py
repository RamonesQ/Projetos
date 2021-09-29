txt = input('Digite algo: ')

print(f'O tipo primitivo desse valor é:{type(txt)}')
print(f'Está em branco? {txt.isspace()}')
print(f'É um numérico? {txt.isnumeric()}')
print(f'É alfabético? {txt.isalpha()}')
print(f'É alfanumérico? {txt.isalnum()}')
print(f'Está em maiusculo? {txt.isupper()}')
print(f'Está em minusculo? {txt.islower()}')
