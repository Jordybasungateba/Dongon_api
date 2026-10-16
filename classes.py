from typing import Annotated, List, Optional

from pydantic import BaseModel, Field, StringConstraints, constr


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

class HeroValidation(BaseModel): 
    id: Optional[int]= Field(default=None, ge=0, description="id is not required")
    name: str = Field(min_length=4)
    nick_name: str = Field(min_length=4)
    full_name: str = Field(min_length=4)
    occupation: List[Annotated[str, StringConstraints(min_length=4)]]
    powers: List[Annotated[str, StringConstraints(min_length=4)]]
    hobby: List[Annotated[str, StringConstraints(min_length=4)]]
    type: str = Field(min_length=4)
    rank: int = Field(ge=0, le=10)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Superman",
                "nick_name": "Clark Kent",
                "full_name": "Kal-El",
                "occupation": ["Journalist", "Hero"],
                "powers": ["Super strength", "Flight", "X-ray vision"],
                "hobby": ["Reading", "Helping people"],
                "type": "Alien",
                "rank": 10
            }
        }
    }
