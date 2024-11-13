from fastapi import APIRouter
from src.schemas.predictBody import PredictBody
from src.controllers.modelController import predict
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/model",
    tags=["model"],
    responses={404: {"description": "Not found"}},
    
)

@router.get("/",)
async def read_root():
    return {"Hello": "World from model"}

@router.post("/predict",)
async def analyze(body: PredictBody):
    # call controller compiler
    try:
        return predict(body)

    except Exception as e:
        print(e)
        return JSONResponse(status_code=400, content={"message": str(e)})
    