from save_json import writeAJson
from database import Database

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

def getPokemonByDex(number: int):
    foundPokemon = db.collection.find_one({"id": number})

    if not foundPokemon:
        print("Dados não encontrados!!")
        return None

    writeAJson(foundPokemon, foundPokemon["name"]["english"].lower())
    return foundPokemon

def getPokemonBytype(type):
    foundPokemon = db.collection.find({"type": type})

    if not foundPokemon:
        print("Dados não encontrados!!")
        return None

    writeAJson(foundPokemon, f"pokemon_{type.lower()}")
    return foundPokemon

def getPokemonByName(name):
    foundPokemon = db.collection.find_one({"name.english": {"$eq": name}})

    if not foundPokemon:
        print("Dados não encontrados!!")
        return None

    writeAJson(foundPokemon, f"{name.lower()}")
    return foundPokemon

def getPokemonByAttack(operator, value: int):
    foundPokemon = db.collection.find({"base.Attack": {f"${operator}": value}})

    if not foundPokemon:
        print("Dados não encontrados!!")
        return None

    writeAJson(foundPokemon, f"attack_{operator.lower()}_{value}")
    return foundPokemon

def getPokemonByHP(operator, value: int):
    foundPokemon = db.collection.find({"base.HP": {f"${operator}": value}})

    if not foundPokemon:
        print("Dados não encontrados!!")
        return None

    writeAJson(foundPokemon, f"HP_{operator.lower()}_{value}")
    return foundPokemon

bulbasaur = getPokemonByDex(1)
grass = getPokemonBytype("Grass")
charmander = getPokemonByName("Charmander")
attackGte50 = getPokemonByAttack("gte", 50)
HPLte50 = getPokemonByHP("lte", 50)
