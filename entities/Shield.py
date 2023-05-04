#direções possíveis (provavelmente colocar isso em outro arquivo)
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

class Shield:
    def __init__(self, direction: int):
        self._direction = direction

    # decidir se a logica do escudo deve
    # permanecer nesta classe ou na do player
    pass