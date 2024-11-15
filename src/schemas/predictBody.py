from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class PredictBody(BaseModel):
    cross_training: bool
    km4week: float           
    sp4week: float

class PredictBody2(BaseModel):
    GENDER: Gender
    AGE: int
    ATMOS_PRESS_mbar: float
    AVG_TEMP_C: float