# pip install mysql.connector
import mysql.connector

conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='[your_password]',
    database='[your_database]'
)

cursor = conexao.cursor()

# CRUD

# CREATE
# nome = "Clock"
# preco = 250
# estoque = 50
# comando = f'INSERT INTO product (id, nome, preco, estoque) VALUES (2, "{nome}", {preco}, {estoque});'
# cursor.execute(comando)
# conexao.commit() # editar o banco de dados

# READ
# comando = 'SELECT * FROM product'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)

# UPDATE
# preco = 300
# comando = f'UPDATE product SET preco = {preco} WHERE id = 1'
# cursor.execute(comando)
# conexao.commit() # editar o banco de dados

# DELETE
# comando = 'DELETE FROM product WHERE id = 1'
# cursor.execute(comando)
# conexao.commit()

cursor.close()
conexao.close()