from save_json import writeAJson
from database import Database

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})


bulbasaur = getPokemonByDex(1)
writeAJson(bulbasaur, "bulbasaur")
