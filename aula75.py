# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


"""def duplicate(numero):
    return numero * 2

print(duplicate(5))

print(' ')

def triplicate(numero):
    print(f'O tripo do numero {numero}: ')
    return numero * 3
    
print(triplicate(7))

print(' ')

def quadruplicam(numero):
    return numero * 4

print(quadruplicam(18))"""

# solucao

# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

    