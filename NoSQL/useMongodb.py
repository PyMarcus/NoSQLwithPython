from pymongo import MongoClient
import datetime

"""
Realizando as definições.
Até inserir algo no mongodb, nada é ,de fato, criado.
"""
# conectando:
connection = MongoClient('localhost', 27017)

#uma única instancia do mongo db suporta vários databases
db = connection.cadastrodb  # apenas isso é suficiente para criar um db

#criando a coleção de documentos(tabela)
collection = db.cadastrodb
print(collection)

#dados no mongodb são representados como arquivos json
# em python, utiliza-se dicionários

"""
Inserir dados
"""
post1 = {
    "código": "ID-9998887",
    "produto": "Geladeira",
    "marcas": ["brastemp", "consul", "elecrolux"],
    "data_cadastro":datetime.datetime.utcnow()
}

collection = db.posts
post_id = collection.insert_one(post1)  #insere o post na tabela
var = post_id.inserted_id # o id será automaticamente se ainda não existir
print(var)  # o resultado é um  código de identificação, tipo um hash


"""
Utilizar um cursor
"""
# a função find retorna um cursor
for post in collection.find():
    print(post)

#verificar o nome do database:
print(db.name)

# verificar as coleções disponíveis
print(db.collection_names())