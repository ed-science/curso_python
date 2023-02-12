"""
Interpolação básica de strings (da linguagem C)
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))


nome = 'Edson'
preco = 10000.9898982
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %05X' % (1500, 1500))

print('O hexadecimal de %d é %05X' % (2500, 3400))