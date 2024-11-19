# Exercícios
try:
    primeiro_valor = int(input('Digite um valor: '))
    segundo_valor = int(input('Digite outro valor: '))

    if primeiro_valor > segundo_valor:
        print('O valor: ', primeiro_valor , ' é maior do que: ', segundo_valor)
    elif segundo_valor > primeiro_valor:
        print('O valor: ', segundo_valor, ' é maior do que: ', primeiro_valor)
    else:
        print('Os valores de inseridos são iguais: ', primeiro_valor)
except ValueError:
    print('Insira um valor válido')