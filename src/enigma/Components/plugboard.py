class Plugboard():
    def __init__(self, settings: str) -> None:
        self._board: dict[str, str] = {}

        if settings == "":
            return

        for group in settings.split(";", 9):
            letters = group.split("-", 1)
            self._board[letters[0]] = letters[1]

    def substitute(self, letter: str) -> str:
        for key, value in self._board.items():
            if letter == key:
                return value
            elif letter == value:
                return key

        return letter