# Conversão de tipos ou coerção.
# Type Convertion, Typecastng, Coertion
# É o ato de converter um tipo em outro

# Tipos Imutáveis e Primitivos: str, int, float, bool

''' 
print('1' + 1) # Erro de concatenação de string e inteiro
'''
print('a' + 'b') #Concatenação (Junção de Strings)

# ----

print(int('1'), type(int('1'))) # Conversão de String para Inteiro
print(type(float('1') + 1)) # Conversão

# ----

print(bool(''))
print(bool('1'))

# ----

print(str(11) + 'b')