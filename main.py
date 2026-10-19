from fastapi import Body, FastAPI, Query, Path, HTTPException
from classes import Hero, HeroValidation
from hereos import  HEROES
from utils import find_proper_hero_id
from starlette import status
from database import DbDependency, engine
from sqlalchemy import text
import models

# initialisation de l'application 
app=FastAPI()
models.Base.metadata.create_all(bind=engine)  # create the database tables

@app.get("/", status_code=status.HTTP_200_OK)
async def  heartbeat(db: DbDependency):
    """test de disponibilité de l'application"""
    try:
        # test de la connexion à la base de données
        db.execute(text("SELECT 1"))
        return {"message": "Application is running and database connection is successful."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/heroes")
async def get_heroes(db: DbDependency):
    """renvoie la liste des héros"""
    return db.query(models.Heroes).order_by(models.Heroes.id.asc()).all()


# Query parameters
@app.get("/heroes/type", status_code=status.HTTP_200_OK)
async def get_all_heroes_by_type(db: DbDependency, hero_type:str= Query()):
    """renvoie la liste des héros par type"""
    results = db.query(models.Heroes).filter(models.Heroes.type.ilike(f"%{hero_type}%")).all()
    return results

@app.get("/heroes/rank", status_code=status.HTTP_200_OK)
async def get_all_heroes_by_rank(db: DbDependency, hero_rank:int= Query(ge=0 , le=100)):
    """renvoie la liste des héros par rang"""
    results = db.query(models.Heroes).filter(models.Heroes.rank >= hero_rank).all()
    return results

#path parameters
@app.get("/heroes/id/{hero_id}", status_code=status.HTTP_200_OK)
async def get_hero_by_id(db: DbDependency, hero_id:int = Path(gt=0)): 
    """renvoie un hero par son identifiant"""
    hero = db.query(models.Heroes).filter(models.Heroes.id == hero_id).first()
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"hero with id {hero_id} not found")
    return hero


@app.get("/heroes/nick_name/{hero_nick_name}", status_code=status.HTTP_200_OK)
async def get_hero_by_nick_name(db: DbDependency, hero_nick_name:str = Path()):
    """renvoie un hero par son surnom"""
    hero = db.query(models.Heroes).filter(models.Heroes.nick_name.ilike(f"%{hero_nick_name}%")).first()
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"hero with nick name {hero_nick_name} not found")
    return hero


# Requetes de creation de hero
@app.post("/hero/create", status_code=status.HTTP_201_CREATED)
async def create_hero(db: DbDependency, hero_body: HeroValidation = Body()):
    """creer un hero"""
    new_hero = models.Heroes(**hero_body.model_dump(exclude={"id"}))
    db.add(new_hero)
    db.commit()
    return new_hero


@app.put("/hero/update", status_code=status.HTTP_204_NO_CONTENT)
async def update_hero(db: DbDependency, hero_body: HeroValidation = Body()): 
    """mettre a jour un hero """
   
    hero = db.query(models.Heroes).filter(models.Heroes.id == hero_body.id).first()
    if not  hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"hero with id {hero_body.id} not found")
    hero.nick_name = hero_body.nick_name
    hero.full_name = hero_body.full_name
    hero.name = hero_body.name
    hero.type = hero_body.type
    hero.rank = hero_body.rank
    db.add(hero)
    db.commit()


@app.delete("/hero/delete/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hero(db: DbDependency, hero_id:int = Path(gt=0)):
    """supprimer un hero"""
    hero = db.query(models.Heroes).filter(models.Heroes.id == hero_id).first()
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"hero with id {hero_id} not found")
    db.delete(hero)
    db.commit()
        