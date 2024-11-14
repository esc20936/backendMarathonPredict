from pydantic import BaseModel

class PredictBody(BaseModel):
    cross_training: bool
    km4week: float           
    sp4week: float

class PredictBody2(BaseModel):
    GENDER: str
    AGE: int
    ATMOS_PRESS_mbar: float
    AVG_TEMP_C: float