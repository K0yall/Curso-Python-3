""" 
Exercício
Peça ao usuário para digitar seu nome;
Peça ao usuário para digitar sua idade;
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} OK
        Seu nome invertido é {nome invertido} OK
        Se nome contém (ou não) espaços
        Se nome tem {n} letras OK
        A primeira letra do seu nome é {letra} OK
        A última letra do seu nome é {letra} OK
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou os campos vazios."
"""
try:
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))

    print(f'Seu nome é: {nome}')
    print(f'Sua idade é: {idade}')
    print('Seu nome invertido é: ',nome[::-1])

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome contém: {len(nome)} letras.' )
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')

except ValueError:
    print('Desculpe, você deixou os campos vazios.')