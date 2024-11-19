# Exercícios

nome = input('Informe o seu nome: ')
altura = float(input('Informe a sua altura em metros: '))
peso = int(input('Informe o seu peso atual: '))
imc = peso / (altura ** 2)

print('Você se chama ', nome, ' e tem ', altura, ' metros de altura.')
print('Você pesa ', peso, 'kg ' 'e seu Índice de massa corporal(IMC) é ', imc)