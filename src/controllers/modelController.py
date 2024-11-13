from src.schemas.predictBody import PredictBody
from src.helpers.loadModel import loadModel
from src.helpers.formatTime import formatTime
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