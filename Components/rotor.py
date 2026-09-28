from __future__ import annotations

class Rotor():
    def __init__(self, wiring: str, position: str, turnover: str, next_rotor: Rotor | None = None) -> None:
        self._wiring = wiring
        self._position = position
        self._turnover = turnover
        self._next_rotor = next_rotor

    def advance(self) -> None:
        if ord(self._position)  == 90:
            self._position = chr(65)
        else:
            self._position = chr(ord(self._position) + 1)

        if self._next_rotor is not None and self._position == self._turnover:
            self._next_rotor.advance()

    def encrypt(self, letter: str) -> str:        
        return self._wiring[(ord(letter) - 65 + (ord(self._position) - 65)) % 26]

    def reverse(self, letter: str) -> str:
<<<<<<< HEAD
        return chr(65 + self._wiring.find(letter))
=======
        #LETTER = K, POSITION = C
        position = self._wiring.find(letter) - (ord(self._position) - 65)
        
        if position >= 0:
            return chr(65 + position)
        else:
            return chr(91 + position)

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, new: str) -> None:
        if len(new) != 1:
            self._position = "A"
        else:
            self._position = new.upper()
>>>>>>> e5c5e182179a7a1e51fd7257b75473153de920b3
