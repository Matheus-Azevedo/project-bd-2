from pymongo import MongoClient  # type: ignore

# Conetando com MySQL local
SQLALCHEMY_DATABASE_URI = (
    "mysql://root:local_root_password@localhost:3306/local_mysql_db"
)

# Conectando com Mongodb local
cliente = MongoClient("mongodb://localhost:27017")
mongodb = cliente["banco_web"]
pedidos_collection = mongodb["pedidos"]
