import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#              'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#               'nome TEXT,'
#               'peso REAL'
#               ')')

""" cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))

cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': 'Joaozinho', 'peso': 75.4}  
)
cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Morgan', 'peso': 90}  
) """
       
# conexao.commit()

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
               {'peso': 80})
    
conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
   identificador, nome, peso = linha
   
   print(identificador, nome, peso)
   
   print(identificador)


#cursor.close()
#conexao.close()