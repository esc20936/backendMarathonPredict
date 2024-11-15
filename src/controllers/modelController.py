from src.schemas.predictBody import PredictBody, PredictBody2
from src.helpers.formatInput import transform_input
from src.helpers.loadModel import loadModel
from src.helpers.formatTime import formatTime, formatTime2
from src.helpers.category import categorize_time
import pandas as pd

def predict(body: PredictBody):
    df = pd.DataFrame([body.dict()])
    model = loadModel()
    prediction = model.predict(df)
    prediction = [round(prediction[0], 3)]
    time = formatTime(prediction[0])
    category = categorize_time(prediction[0])
    return {"time": time, "category": category}


def predictV2(body: PredictBody2):
    data = transform_input(body)
    df = pd.DataFrame([data])
    model = loadModel(v2=True)
    prediction = model.predict(df)
    prediction = [round(prediction[0], 3)]
    time = formatTime2(prediction[0])
    category = categorize_time(prediction[0])
    print({"time": time, "category": category})
    return {"time": time, "category": category}