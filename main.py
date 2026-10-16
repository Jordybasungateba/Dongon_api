from fastapi import Body, FastAPI, Query, Path, HTTPException
from classes import Hero, HeroValidation
from hereos import  HEROES
from utils import find_proper_hero_id
from starlette import status

# initialisation de l'application 
app=FastAPI()

@app.get("/")
async def  heartbeat():
    """test de disponibilité de l'application"""
    return "app running"

@app.get("/heroes")
async def get_heroes():
    """renvoie la liste des héros"""
    return HEROES


# Query parameters
@app.get("/heroes/type", status_code=status.HTTP_200_OK)
async def get_all_heroes_by_type(hero_type:str= Query()):
    """renvoie la liste des héros par type"""
    heroes_by_type=[hero for hero in HEROES if hero.type.casefold() in hero_type.lower().casefold()]
    return heroes_by_type

@app.get("/heroes/rank", status_code=status.HTTP_200_OK)
async def get_all_heroes_by_rank(hero_rank:int= Query(ge=0 , le=100)):
    """renvoie la liste des héros par rang"""
    heroes_by_rank=[hero for hero in HEROES if hero.rank >= hero_rank]
    return heroes_by_rank

#path parameters
@app.get("/heroes/id/{hero_id}", status_code=status.HTTP_200_OK)
async def get_hero_by_id(hero_id:int = Path(gt=0)): 
    """renvoie un hero par son identifiant"""
    for hero in HEROES:
        if hero.id == hero_id:
            return hero
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"hero with id {hero_id} not found")


@app.get("/heroes/nick_name/{hero_nick_name}", status_code=status.HTTP_200_OK)
async def get_hero_by_nick_name(hero_nick_name:str = Path()):
    """renvoie un hero par son surnom"""
    for hero in HEROES:
        if hero.nick_name.casefold() == hero_nick_name.lower().casefold():
            return hero
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"hero with nick name {hero_nick_name} not found")


# Requetes de creation de hero
@app.post("/hero/create", status_code=status.HTTP_201_CREATED)
async def create_hero(hero_body: HeroValidation = Body()):
    """creer un hero"""
    new_hero = Hero(**hero_body.model_dump())
    # print(type(new_hero))
    # pass
    find_proper_hero_id(new_hero)
    HEROES.append(new_hero)
    return new_hero


@app.put("/hero/update", status_code=status.HTTP_204_NO_CONTENT)
async def update_hero(hero_body: HeroValidation = Body()): 
    """mettre a jour un hero """
    hero_changed = False
    for i in range(len(HEROES)):
        if HEROES[i].id == hero_body.id:
            hero_changed = True
            HEROES[i] = Hero(**hero_body.model_dump())

    if not hero_changed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"hero with id {hero_body.id} not found")


@app.delete("/hero/delete/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hero(hero_id:int = Path(gt=0)):
    """supprimer un hero"""
    hero_changed = False
    for i in range(len(HEROES)):
        if HEROES[i].id == hero_id:
            HEROES.pop(i)
            hero_changed = True
            break

    if not hero_changed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"hero with id {hero_id} not found")