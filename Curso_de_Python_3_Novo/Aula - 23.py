# Operadores Lógicos
# And - Or - Not
# Not True = False
# Not False = True

senha = input('Senha: ')

if senha == '123456':
    print('Entrou')
else:
    print('Senha incorreta.')

# if senha!= '123456':
    # print('Senha incorreta.')

if not senha:
    print('Você não digitou nada')

print(not True) #False
print(not False) #True

