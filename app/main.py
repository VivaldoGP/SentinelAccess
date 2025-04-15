from fastapi import FastAPI
from .routers import auth, public

app = FastAPI()
app.include_router(auth.router)
app.include_router(public.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}