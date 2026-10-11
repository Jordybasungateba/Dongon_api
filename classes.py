from typing import List


class Hero: 
    """Classe représentant un héros"""
    id: int
    name: str
    nick_name: str
    full_name: str
    occupation: List[str]
    powers: List[str]
    hobby: List[str]
    type: str
    rank: int

    def __init__(self, id:int, name:str, nick_name:str, full_name:str, occupation:List[str], powers:List[str], hobby:List[str], type:str, rank:int):
        self.id = id
        self.name = name
        self.nick_name = nick_name
        self.full_name = full_name
        self.occupation = occupation
        self.powers = powers
        self.hobby = hobby
        self.type = type
        self.rank = rank