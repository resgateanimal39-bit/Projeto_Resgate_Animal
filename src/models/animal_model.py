from tinydb import TinyDB


db = TinyDB("src/data/db.json")
tutores = db.table("tutores")
pets = db.table("pets")
usuarios = db.table("usuarios")

