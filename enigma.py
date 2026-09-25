from Components.rotor import Rotor
from Components.reflector import Reflector

ROTOR_1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "A", "Q")
#ROTOR_2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "A", "E")
#ROTOR_3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "A", "V")
REFLECTOR = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

def rotors(letter: str) -> str:
    result = ROTOR_1.encrypt(letter)
    print(result)

    result = REFLECTOR.encrypt(result)
    print(result)
    
    result = ROTOR_1.reverse(result)
    print(result)

    ROTOR_1.advance()
    
    return result