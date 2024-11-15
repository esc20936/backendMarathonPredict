from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi.responses import JSONResponse, FileResponse
from src.routes.model import router as model_router
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(model_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

