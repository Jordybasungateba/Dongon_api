from typing import Annotated, List, Literal, Optional

from pydantic import BaseModel, Field, StringConstraints, constr, field_validator


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


# ---------------------------------------- Player Validation ----------------------------------------

AllowedRoles = Literal["Controler", "defener", "striker", "leader"]

class PlayerValidation(BaseModel):
    """Classe représentant un joueur avec validation des champs"""
    username: str = Field(min_length=4, description="Le nom d'utilisateur doit contenir au moins 4 caractères")
    first_name: str = Field(min_length=4, description="Le prénom doit contenir au moins 4 caractères")
    last_name: str = Field(min_length=4, description="Le nom de famille doit contenir au moins 4 caractères")
    email: str = Field(min_length=4, description="L'adresse email doit contenir au moins 4 caractères")
    password: str = Field(min_length=8, description="Le mot de passe doit contenir au moins 8 caractères")
    role: AllowedRoles = Field(min_length=4, description="Le rôle doit contenir au moins 4 caractères")

    @field_validator("role", mode="before")
    def validate_role(cls, value):
        """Valide le rôle du joueur"""
        if value not in ["Controler", "defener", "striker", "leader"]:
            raise ValueError("Le rôle doit être l'un des suivants : Controler, defener, striker, leader")
        return value

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "player1",
                "first_name": "John",
                "last_name": "Does",
                "email": "player@exemple.com",
                "password": "password123",
                "role": "Controler"
            }
        }}




class Token(BaseModel):
    access_token: str
    token_type: str