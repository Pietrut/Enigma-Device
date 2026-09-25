class Rotor():
    def __init__(self, wiring: str, position: str, turnover: str) -> None:
        self._wiring = wiring
        self._position = position
        self._turnover = turnover

    def advance(self) -> None:
        if ord(self._position)  == 90:
            self._position = chr(65)
        else:
            self._position = chr(ord(self._position) + 1)

    def encrypt(self, letter: str) -> str:        
        return self._wiring[(ord(letter) - 65 + (ord(self._position) - 65)) % 26]