# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'Pedro', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'C'},
    {'nome': 'José', 'nota': 'D'},
    {'nome': 'Joana', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    
]

def orderna(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=orderna)
grupos = groupby(alunos_agrupados, key=orderna)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)