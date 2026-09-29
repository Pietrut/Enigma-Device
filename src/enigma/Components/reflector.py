class Reflector():
    def __init__(self, wiring: str) -> None:
        self._wiring = wiring

    def encrypt(self, letter: str) -> str:
        return self._wiring[ord(letter) - 65]