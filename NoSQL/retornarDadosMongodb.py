import pymongo

# conectando a conexão padrão
client_con = pymongo.MongoClient()
#para conectar a uma colecao específica db["nomedacolecao"]
# listando os bancos
bancos = client_con.database_names()

# definir objeto db
db = client_con.cadastrodb

# listando as conexões disponíveis

print(db.collection_names())

# criando uma coleção

db.create_collection("myNewCollection")

#listando novamente

print(db.collection_names())

#inserir dados no novo db
db.myNewCollection.insert_one({
    'titulo':'mongodb com python',
    'descrição': 'mongodb é um banco de dados noSql'
})

# retornando o documento criado:
variavel = db.myNewCollection.find_one()
print(variavel)

col = db["posts"] #conecta a posts
print(col)

#conta os documentos
print(col.count())

redoc = col.find_one() #pega 1 documento
print(redoc)