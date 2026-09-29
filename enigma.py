from Components.rotor import Rotor
from Components.reflector import Reflector

ROTORS: dict[str, tuple[str, str]] = {
    "I": ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V": ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
}

class Enigma():
    def __init__(self, numbers: str) -> None:
        self._reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        self._rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "A", "V")
        self._rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "A", "E", self._rotor3)
        self._rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "A", "Q", self._rotor2)

        r1_assigned = r2_assigned = r3_assigned = False
        for number in numbers.split("-", 2):
            if number not in ROTORS:
                break

            rotor = ROTORS[number]
            if not r3_assigned:
                self._rotor3 = Rotor(rotor[0], "A", rotor[1])
                continue

            if not r2_assigned:
                self._rotor2 = Rotor(rotor[0], "A", rotor[1], self._rotor3)
                continue

            if not r1_assigned:
                self._rotor1 = Rotor(rotor[0], "A", rotor[1], self._rotor2)
                continue

    def _encrypt(self, letter: str) -> str:
        result = self._rotor1.encrypt(letter)
        result = self._rotor2.encrypt(result)
        result = self._rotor3.encrypt(result)
    
        result = self._reflector.encrypt(result)
    
        result = self._rotor3.reverse(result)
        result = self._rotor2.reverse(result)
        result = self._rotor1.reverse(result)
    
        self._rotor1.advance()
        
        return result

    def adjust(self, code: str) -> None:
        self._rotor1.position = code[2]
        self._rotor2.position = code[1]
        self._rotor3.position = code[0]

    def start(self, text: str) -> str:
        result = ""
    
        for letter in text:
            if ord(letter) >= 65 and ord(letter) <= 90:
                result += self._encrypt(letter)
            else:
                result += letter
    
        return result