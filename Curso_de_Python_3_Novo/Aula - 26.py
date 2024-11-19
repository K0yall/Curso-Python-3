""" 
Formatação Básica de Strings
Ex: 0>-100,.1f
"""

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel:7>10}')
print(f'{variavel:8<10}')
print(f'{variavel:9^10}')

print(f'{1000.684646468464863:,.1f}')
print(f'{1000.684646468543153:-,.1f}')
print(f'{1000.684987684635464863:+,.1f}')
print(f'{1000.315317863:2=+,.1f}')