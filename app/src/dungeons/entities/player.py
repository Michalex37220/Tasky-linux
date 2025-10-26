from .base_entity import BaseEntity

class Player(BaseEntity):

    def __init__(self, name:str, hp:int, strength:int, defense:int, current_xp:int, total_xp:int) -> None:
        super().__init__(hp, strength, defense, name)
