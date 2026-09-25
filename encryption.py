from rotor import Rotor

ROTOR_1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "A", "Q")
ROTOR_2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "A", "E")
ROTOR_3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "A", "V")
REFLECTOR = Rotor("YRUHQSLDPXNGOKMIEBFZCWVJAT")

def rotors(letter: str) -> str:
    result = ROTOR_1.encrypt(letter)
    #result = ROTOR_2.encrypt(result)
    #result = ROTOR_3.encrypt(result)

    result = REFLECTOR.encrypt(result)

    #result = ROTOR_3.encrypt(result)
    #result = ROTOR_2.encrypt(result)
    result = ROTOR_1.encrypt(result)

    ROTOR_1.advance()
    
    return result