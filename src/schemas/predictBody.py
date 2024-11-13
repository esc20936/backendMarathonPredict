from pydantic import BaseModel

class PredictBody(BaseModel):
    cross_training: bool
    km4week: float           
    sp4week: float           