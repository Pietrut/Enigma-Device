from Components.rotor import Rotor
from Components.reflector import Reflector

class Enigma():
    def __init__(self) -> None:
        self._rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "A", "V")
        self._rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "A", "E", self._rotor3)
        self._rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "A", "Q", self._rotor2)
        self._reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

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

    def adjust(self) -> None:
        code = input("Enter code: ")
        self._rotor1.position = code[2]
        self._rotor2.position = code[1]
        self._rotor3.position = code[0]

    def lights(self, result: str) -> None:
        print("\n" + result)

    def start(self) -> None:
        text = input("Enter Text:\n").upper()
        result = ""
    
        for letter in text:
            if ord(letter) >= 65 and ord(letter) <= 90:
                result += self._encrypt(letter)
            else:
                result += letter
    
        self.lights(result)