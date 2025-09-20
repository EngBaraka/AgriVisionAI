from fastapi import FastAPI
from app.routers import health,users  # import our router

app = FastAPI()

# include router
app.include_router(health.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Welcome to AgriVisionAI Backend"}
