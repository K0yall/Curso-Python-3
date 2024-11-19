# Exercícios

nome = input('Informe o seu nome: ') 
sobrenome = input('Informe o seu sobrenome: ')
idade = int(input('Informe a sua idade: '))
nascimento = int(input('Informe o ano de seu nascimento: '))
altura = int(input('Informe a sua altura em centímetros: '))
altura_metros = float(input('Informe a sua altura em metros: '))
maior_idade = idade >= 18


print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento:', nascimento)
print('É maior de idade?:', 'Sim' if maior_idade else 'Não')
print('Altura em centímetros:', altura)
print('Altura em metros:', altura_metros)
