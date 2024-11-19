""" 
Introdução ao try/except
try → tentar executar o código
except → ocorreu algum erro ao tentar executar
"""

try:
    ...
except:
    ...


n_string = input('Vou dobrar o nmr que você digitar: ')
if (n_string.isdigit):
    n_float = float(n_string)
    print(f'O dobro de {n_string} é {n_float*2:.0f}')
else:
    print('Isso não é um número') 