import pytest
from src.pykemon import pykemon

class Tests:
    def test_sanity_check(self):
        assert(pykemon.pokemons), "able to get pokemons"
        expected = True 
        actual = True 
        assert actual == expected, "sanity check incomplete."
    def test_p_num_invalidin(self):
        out = pykemon.p_num("")
        assert(out=="Pokemon not found."), f"should return error message for an empty string"
        out = pykemon.p_num("ewasdf")
        assert(out=="Pokemon not found."), f"should return error message for invalid input"
        out = pykemon.p_num(5)
        assert(out=="Pokemon not found."), f"should return error message for invalid type"
    def test_p_num_lower(self):
        out = pykemon.p_num("bulbasaur number")
        assert(out=="1"), f"wrong number returned. pokemon = bulbasaur expected=1 actual={out} "
        out = pykemon.p_num("ivysaur number")
        assert(out=="2"), f"wrong number returned. pokemon = ivysaur expected=2 actual={out} "
        out = pykemon.p_num("venusaur number")
        assert(out=="3"), f"wrong number returned. pokemon = venusaur expected=3 actual={out} "
        out = pykemon.p_num("charmander number")
        assert(out=="4"), f"wrong number returned. pokemon = charmander expected=4 actual={out} "
        out = pykemon.p_num("charmeleon number")
        assert(out=="5"), f"wrong number returned. pokemon = charmeleon expected=5 actual={out} "
        out = pykemon.p_num("charizard number")
        assert(out=="6"), f"wrong number returned. pokemon = charizard expected=6 actual={out} "
        out = pykemon.p_num("squirtle number")
        assert(out=="7"), f"wrong number returned. pokemon = squirtle expected=7 actual={out} "
        out = pykemon.p_num("wartortle number")
        assert(out=="8"), f"wrong number returned. pokemon = wartortle expected=8 actual={out} "
        out = pykemon.p_num("blastoise number")
        assert(out=="9"), f"wrong number returned. pokemon = blastoise expected=9 actual={out} "
        out = pykemon.p_num("pikachu number")
        assert(out=="25"), f"wrong number returned. pokemon = pikachu expected=25 actual={out} "
        out = pykemon.p_num("raichu number")
        assert(out=="26"), f"wrong number returned. pokemon = raichu expected=26 actual={out} "
    def test_p_num_upper(self):
        out = pykemon.p_num("Bulbasaur number")
        assert(out=="1"), f"wrong number returned when input is upper case. pokemon = bulbasaur expected=1 actual={out} "
        out = pykemon.p_num("ivYsaur number")
        assert(out=="2"), f"wrong number returned when input is upper case.. pokemon = ivysaur expected=2 actual={out} "
        out = pykemon.p_num("veNUsaur number")
        assert(out=="3"), f"wrong number returned when input is upper case.. pokemon = venusaur expected=3 actual={out} "
        out = pykemon.p_num("charmandeR number")
        assert(out=="4"), f"wrong number returned when input is upper case.. pokemon = charmander expected=4 actual={out} "
        out = pykemon.p_num("charmeleON number")
        assert(out=="5"), f"wrong number returned when input is upper case.. pokemon = charmeleon expected=5 actual={out} "
        out = pykemon.p_num("CHARIZARD number")
        assert(out=="6"), f"wrong number returned when input is upper case.. pokemon = charizard expected=6 actual={out} "
        out = pykemon.p_num("squirTLE number")
        assert(out=="7"), f"wrong number returned when input is upper case.. pokemon = squirtle expected=7 actual={out} "
        out = pykemon.p_num("wartorTle number")
        assert(out=="8"), f"wrong number returned when input is upper case.. pokemon = wartortle expected=8 actual={out} "
        out = pykemon.p_num("blastOise number")
        assert(out=="9"), f"wrong number returned when input is upper case.. pokemon = blastoise expected=9 actual={out} "
        out = pykemon.p_num("PIKACHU number")
        assert(out=="25"), f"wrong number returned when input is upper case.. pokemon = pikachu expected=25 actual={out} "
        out = pykemon.p_num("Raichu number")
        assert(out=="26"), f"wrong number returned when input is upper case.. pokemon = raichu expected=26 actual={out} "
    def test_p_type_invalidin(self):
        out = pykemon.p_type("")
        assert(out=="Pokemon not found."), f"should return error message for an empty string"
        out = pykemon.p_type("ewasdf")
        assert(out=="Pokemon not found."), f"should return error message for invalid input"
        out = pykemon.p_type(5)
        assert(out=="Pokemon not found."), f"should return error message for invalid type"
    def test_p_type(self):
        out = pykemon.p_type("bulbasaur type")
        assert(out=="Grass"), f"wrong type returned. pokemon = bulbasaur expected=Grass actual={out} "
        out = pykemon.p_type("ivysaur type")
        assert(out=="Grass"), f"wrong type returned. pokemon = ivysaur expected=Grass actual={out} "
        out = pykemon.p_type("venusaur type")
        assert(out=="Grass"), f"wrong type returned. pokemon = venusaur expected=Grass actual={out} "
        out = pykemon.p_type("charmander type")
        assert(out=="Fire"), f"wrong type returned. pokemon = charmander expected=Fire actual={out} "
        out = pykemon.p_type("charmeleon type")
        assert(out=="Fire"), f"wrong type returned. pokemon = charmeleon expected=Fire actual={out} "
        out = pykemon.p_type("charizard type")
        assert(out=="Fire"), f"wrong type returned. pokemon = charizard expected=Fire actual={out} "
        out = pykemon.p_type("squirtle type")
        assert(out=="Water"), f"wrong type returned. pokemon = squirtle expected=Water actual={out} "
        out = pykemon.p_type("wartortle type")
        assert(out=="Water"), f"wrong type returned. pokemon = wartortle expected=Water actual={out} "
        out = pykemon.p_type("blastoise type")
        assert(out=="Water"), f"wrong type returned. pokemon = blastoise expected=Water actual={out} "
        out = pykemon.p_type("pikachu type")
        assert(out=="Electric"), f"wrong type returned. pokemon = pikachu expected=Electric actual={out} "
        out = pykemon.p_type("raichu type")
        assert(out=="Electric"), f"wrong type returned. pokemon = raichu expected=Electric actual={out} "
    def test_p_type_upper(self):
        out = pykemon.p_type("bulbasAur type")
        assert(out=="Grass"), f"wrong type returned when input is upper case.. pokemon = bulbasaur expected=Grass actual={out} "
        out = pykemon.p_type("ivySaur type")
        assert(out=="Grass"), f"wrong type returned when input is upper case.. pokemon = ivysaur expected=Grass actual={out} "
        out = pykemon.p_type("veNusaur type")
        assert(out=="Grass"), f"wrong type returned when input is upper case.. pokemon = venusaur expected=Grass actual={out} "
        out = pykemon.p_type("cHarmander type")
        assert(out=="Fire"), f"wrong type returned when input is upper case.. pokemon = charmander expected=Fire actual={out} "
        out = pykemon.p_type("Charmeleon type")
        assert(out=="Fire"), f"wrong type returned when input is upper case.. pokemon = charmeleon expected=Fire actual={out} "
        out = pykemon.p_type("Charizard type")
        assert(out=="Fire"), f"wrong type returned when input is upper case.. pokemon = charizard expected=Fire actual={out} "
        out = pykemon.p_type("squIrtle type")
        assert(out=="Water"), f"wrong type returned when input is upper case.. pokemon = squirtle expected=Water actual={out} "
        out = pykemon.p_type("warTOrtle type")
        assert(out=="Water"), f"wrong type returned when input is upper case.. pokemon = wartortle expected=Water actual={out} "
        out = pykemon.p_type("blastOise type")
        assert(out=="Water"), f"wrong type returned when input is upper case.. pokemon = blastoise expected=Water actual={out} "
        out = pykemon.p_type("pikachU type")
        assert(out=="Electric"), f"wrong type returned when input is upper case.. pokemon = pikachu expected=Electric actual={out} "
        out = pykemon.p_type("RAICHU type")
        assert(out=="Electric"), f"wrong type returned when input is upper case.. pokemon = raichu expected=Electric actual={out} "
    def test_p_evo(self):
        out = pykemon.p_evo("evolve bulbasaur")
        assert(out==pykemon.pokemons["ivysaur"]), f"wrong pokemon. pokemon = bulbasaur"
        out = pykemon.p_evo("evolve ivysaur")
        assert(out==pykemon.pokemons["venusaur"]), f"wrong pokemon. pokemon = ivysaur"
        out = pykemon.p_evo("evolve charmander")
        assert(out==pykemon.pokemons["charmeleon"]), f"wrong pokemon. pokemon = charmander"
        out = pykemon.p_evo("evolve charmeleon")
        assert(out==pykemon.pokemons["charizard"]), f"wrong pokemon. pokemon = charmeleon"
        out = pykemon.p_evo("evolve squirtle")
        assert(out==pykemon.pokemons["watortle"]), f"wrong pokemon. pokemon = squirtle"
        out = pykemon.p_evo("evolve wartortle")
        assert(out==pykemon.pokemons["blastoise"]), f"wrong pokemon. pokemon = wartortle"
        out = pykemon.p_evo("evolve pikachu")
        assert(out==pykemon.pokemons["raichu"]), f"wrong pokemon. pokemon = pikachu"
    def test_p_evo_noevo(self):
        out = pykemon.p_evo("evolve venusaur")
        assert(out=="This pokemon does not evolve."), f"this pokemon should not be able to evolve."
        out = pykemon.p_evo("evolve raichu")
        assert(out=="This pokemon does not evolve."), f"this pokemon should not be able to evolve."
        out = pykemon.p_evo("evolve charizard")
        assert(out=="This pokemon does not evolve."), f"this pokemon should not be able to evolve."
        out = pykemon.p_evo("evolve blastoise")
        assert(out=="This pokemon does not evolve."), f"this pokemon should not be able to evolve."
    def test_p_evo_invalidin(self):
        out = pykemon.p_evo("")
        assert(out=="Pokemon not found."), f"should return error message for an empty string"
        out = pykemon.p_evo("ewasdf")
        assert(out=="Pokemon not found."), f"should return error message for invalid input"
        out = pykemon.p_evo(5)
        assert(out=="Pokemon not found."), f"should return error message for invalid type"
    def test_p_pic_invalidin(self):
        out = pykemon.p_pic("")
        assert(out=="Pokemon not found, please try bulbasaur, charmander, squirtle, or pikachu."), f"should return error message for an empty string"
        out = pykemon.p_pic("ewasdf")
        assert(out=="Pokemon not found, please try bulbasaur, charmander, squirtle, or pikachu."), f"should return error message for invalid input"
        out = pykemon.p_pic(5)
        assert(out=="Pokemon not found, please try bulbasaur, charmander, squirtle, or pikachu."), f"should return error message for invalid type"
    def test_p_pic_bulbasaur(self):
        out = pykemon.p_pic("bulbasaur")
        assert(out==pykemon.pokemons["bulbasaur"]), f"should return a bulbasaur, instead returned {out}"
    def test_p_pic_charmander(self):
        out = pykemon.p_pic("charmander")
        assert(out==pykemon.pokemons["charmander"]), f"should return a charmander, instead returned {out}"
    def test_p_pic_squirtle(self):
        out = pykemon.p_pic("squirtle")
        assert(out==pykemon.pokemons["squirtle"]), f"should return a squirtle, instead returned {out}"
    def test_p_pic_pikachu(self):
        out = pykemon.p_pic("pikachu")
        assert(out==pykemon.pokemons["pikachu"]), f"should return a pikachu, instead returned {out}"
    
