from fastapi import FastAPI, Query, Path
from hereos import  HEROES

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

@app.get("/heroes/type")
async def get_all_heroes_by_type(hero_type:str= Query()):
    """renvoie la liste des héros par type"""
    heroes_by_type=[hero for hero in HEROES if hero.get("type").casefold() in hero_type.lower().casefold()]
    return heroes_by_type

@app.get("/heroes/rank")
async def get_all_heroes_by_rank(hero_rank:int= Query()):
    """renvoie la liste des héros par rang"""
    heroes_by_rank=[hero for hero in HEROES if hero.get("rank") >= hero_rank]
    return heroes_by_rank

@app.get("/heroes/id/{hero_id}")
async def get_hero_by_id(hero_id:int = Path()): 
    """renvoie un hero par son identifiant"""
    for hero in HEROES:
        if hero.get("id")==hero_id:
            return hero


@app.get("/heroes/nick_name/{hero_nick_name}")
async def get_hero_by_nick_name(hero_nick_name:str = Path()):
    """renvoie un hero par son surnom"""
    for hero in HEROES:
        if hero.get("nick_name").casefold() == hero_nick_name.lower().casefold():
            return hero