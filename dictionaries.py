dict_of_pokemon = { 
    "pet1": {
        "name": "Pikachu",
        "type": "electric",
        "next evolution": "Raichu",
        "IQ": "230",
        "fav food": "pikaberries",
        "fav drink": "pikajuice",
        "temperment": "volatile"
        },
    "pet2": {
        "name": "charmander",
        "type": "fire",
        "next evolution": "charmeleon",
        "IQ": "210",
        "fav food": "charberries",
        "fav drink": "charjuice",
        "temperment": "well ballanced"
        },


    "pet3": {
        "name": "mew",
        "type": "pychic",
        "next evolution": "mewtwo",
        "IQ": "240",
        "fav food": "mewberries",
        "fav drink": "mewjuice",
        "temperment": "extremely happy"
        },
    }

print(dict_of_pokemon["pet1"]["fav food"])

del dict_of_pokemon["pet1"]["fav food"]

dict_of_pokemon["pet1"]["fav food"] = "newberries"

print(dict_of_pokemon["pet1"]["fav food"])


print(dict_of_pokemon["pet3"]["fav food"])

del dict_of_pokemon["pet3"]["fav food"]

del dict_of_pokemon["pet3"]["IQ"]

dict_of_pokemon["pet3"]["IQ"] = "2000"

dict_of_pokemon["pet3"]["fav food"] = "IQ berries"

print(dict_of_pokemon["pet3"]["fav food"])

print(dict_of_pokemon["pet3"]["IQ"])



# .keys()
#     list of keys in dictionary

# .vaues()
#     list of vales in dictionary

# .items()
#     list of tuples

# .get()
#     name of a key to get value 2nd value for none exsisting 1st key

# list(casting method)

# .pop remove keys from dict

for dict_i in dict_of_pokemon:
    print(list(dict_i.values())[0])


# from somwhere import specified list



