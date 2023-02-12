"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
""" tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3]) """

nova_string = ''
nova_string += '*L*u*i*z* *O*t*á*v*i*o'

nome = 'Edson Andrade' 

index = 0
new_name = ''


while index < len(nome):
    letra = nome[index]
    new_name += f'*{letra}'
    index += 1

print(new_name)