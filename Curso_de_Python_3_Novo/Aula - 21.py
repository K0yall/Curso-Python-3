# Operadores Lógicos
# And - Or - Not

entrada = input('Para entrar digite [E] e para sair digite [S]: ')

if entrada == 'E' or entrada == 'S':
    senha_digitada = input('Senha: ')
    senha_permitida = '123456'
    
    if entrada == 'E' and senha_digitada == senha_permitida:
        print('Entrar')
    if entrada == 'E' and senha_digitada != senha_permitida:
        print('Senha Inválida')
    elif entrada == 'S':
        print('Sair')
else:
    print('Informe apenas [E] ou [S]')
