"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    print(f'{x=} {y=} {z=}', 'x + y + z', '--' , x + y + z)
    
    
soma(1, 2, 3)
soma(x= 3, z=4, y=3)

print(1, 2, 3, sep='-')