# Operadores in e not in
# Strings são iteráveis

nome = 'Lucas'
print(nome[2])

nome2 = 'Lucas'
print('s' in nome)

print(10*'-')

nome3 = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome3:
    print(f'{encontrar} está em {nome3}')
else:
    print(f'{encontrar} não está em {nome}')