from fastapi import APIRouter, Body, Depends
from typing import Annotated
from classes import PlayerValidation, Token
from models import Players
from database import DbDependency as Db 
from starlette import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from datetime import datetime, timedelta, timezone


router = APIRouter()

# BCRYPT CONFIG
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# JWT CONFIG
JWT_SECRET_KEY = "e47975336b44e036a264a3b099b41663518f7e32aa25ca37c9bb99818af628cfcc98648c6bb14207f01150e4b44280e6d9c2c46703de1448a5b54820e5059864"  # Change
HASHING_ALGORITHM = "HS256"






@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_player(db: Db,player_body: PlayerValidation = Body()):
    """ creation d'un nouveau joueur """
    new_player = Players(
        username=player_body.username,
        first_name=player_body.first_name,
        last_name=player_body.last_name,
        email=player_body.email,
        password=bcrypt_context.hash(player_body.password),
        role=player_body.role
    )
    db.add(new_player)
    db.commit()
    return  new_player


def authenticate_player(db, username: str, password: str):
    """Authentifie un joueur en vérifiant son nom d'utilisateur et son mot de passe"""
    player = db.query(Players).filter(Players.username == username).first()
    if not player:
        return False
    if not bcrypt_context.verify(password, player.password):
        return False
    return player



def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    """Crée un token d'accès JWT pour un joueur authentifié"""
    encoded_data = {
        "sub": username,
        "id": user_id,
        "exp": int((datetime.now(timezone.utc) + expires_delta).timestamp())
    }
    return jwt.encode(encoded_data, JWT_SECRET_KEY, algorithm=HASHING_ALGORITHM)

@router.post("/auth/login", status_code=status.HTTP_200_OK, response_model=Token)
async def login_player(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Db
):
    """Authentifie un joueur et retourne un token d'accès"""
    player_authenticated = authenticate_player(db, form_data.username, form_data.password)
    if not player_authenticated:
        return {"error": "Invalid username or password"}
    token = create_access_token(
        username=player_authenticated.username,
        user_id=player_authenticated.id,
        expires_delta=timedelta(minutes=30)
    )
    return {"message": "Login successful", "access_token": token, "token_type": "bearer"}
