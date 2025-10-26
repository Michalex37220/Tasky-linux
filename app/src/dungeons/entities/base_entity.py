

class BaseEntity:
    """
    The base class for all entities
    """

    def __init__(self, hp:int, strength:int, defense:int, name=None) -> None:
        self.name = name
        self.hp = hp
        self.strength = strength
        self.defense = defense