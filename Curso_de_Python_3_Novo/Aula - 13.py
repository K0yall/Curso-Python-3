# Exercícios

nome = input('Informe o seu nome: ')
altura = float(input('Informe a sua altura em metros: '))
peso = int(input('Informe o seu peso atual: '))
imc = peso / (altura ** 2)

# print('Você se chama ', nome, ' e tem ', altura, ' metros de altura.')
# print('Você pesa ', peso, 'kg ' 'e seu Índice de massa corporal(IMC) é ', imc)

'f-strings'
linha1 = f'{nome} tem {altura:.2f} de altura'
linha2 = f'pesa {peso} quilos e seu imc é'
linha3 = f'{imc:.2f}'

print(linha1)
print(linha2)
print(linha3)