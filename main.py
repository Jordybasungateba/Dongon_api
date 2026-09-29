from fastapi import FastAPI

# initialisation de l'application 
app=FastAPI()

@app.get("/")
async def  heartbeat():
    """test de disponibilité de l'application"""
    return "app running"
