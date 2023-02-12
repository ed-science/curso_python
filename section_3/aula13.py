nome = 'Edson'
altura = 1.80
peso = 80
imc = peso / altura ** 2

linha_1 = f'Nome: {nome} ele pesa: {peso} kg e tem altura de: {altura:,.2f} m'
linha_2 = f'Seu IMC é de: {imc:,.2f}'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)

