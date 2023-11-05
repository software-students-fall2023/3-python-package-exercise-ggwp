import random
from ascii_art_pykemon import pokemons

def p_pic(pokemon):
    pokemon_list = ["charmander", "squirtle", "bulbasaur", "pikachu"]
    random_pokemon = random.choice(pokemon_list)
    if random_pokemon == "bulbasaur":
        return pokemons["bulbasaur"]
    elif random_pokemon == "charmander":
        return pokemons["charmander"]
    elif random_pokemon == "squirtle":
        return pokemons["squirtle"]
    elif pokemon.lower() == "pikachu":
        return pokemons["pikachu"]
    
def p_evo(pokemon):
    if pokemon.lower() == "evolve bulbasaur":
        return pokemons["ivysaur"]
    elif pokemon.lower() == "evolve ivysaur":
        return pokemons["venusaur"]
    elif pokemon.lower() == "evolve charmander":
        return pokemons["charmeleon"]
    elif pokemon.lower() == "evolve charmeleon":
        return pokemons["charizard"]
    elif pokemon.lower() == "evolve squirtle":
        return pokemons["wartortle"]
    elif pokemon.lower() == "evolve wartortle":
        return pokemons["blastoise"]
    elif pokemon.lower() == "evolve pikachu":
        return pokemons["raichu"]
    else:
        return "Pokemon not found."

def p_type(pokemon):
    if pokemon.lower() == "bulbasaur type" or pokemon.lower() == "ivysaur type" or pokemon.lower() == "venusaur type":
        return "Grass"
    elif pokemon.lower() == "charmander type" or pokemon.lower() == "charmeleon type" or pokemon.lower() == "charizard type":
        return "Fire"
    elif pokemon.lower() == "squirtle type" or pokemon.lower() == "wartortle type" or pokemon.lower() == "blastoise type":
        return "Water"
    elif pokemon.lower() == "pikachu type" or pokemon.lower() == "raichu type":
        return "Electric"
    else:
        return "Pokemon not found."

def p_num(pokemon):
    if pokemon.lower() == "bulbasaur number":
        return "1"
    elif pokemon.lower() == "ivysaur number":
        return "2"
    elif pokemon.lower() == "venusaur number":
        return "3"
    elif pokemon.lower() == "charmander number":
        return "4"
    elif pokemon.lower() == "charmeleon number":
        return "5"
    elif pokemon.lower() == "charizard number":
        return "6"
    elif pokemon.lower() == "squirtle number":
        return "7"
    elif pokemon.lower() == "wartortle number":
        return "8"
    elif pokemon.lower() == "blastoise number":
        return "9"
    elif pokemon.lower() == "pikachu number":
        return "25"
    elif pokemon.lower() == "raichu number":
        return "26"
    else:
        return "Pokemon not found."
