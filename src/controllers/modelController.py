from src.schemas.predictBody import PredictBody, PredictBody2, trainBody, trainBody2
from src.helpers.formatInput import transform_input
from src.helpers.loadModel import loadModel
from src.helpers.formatTime import formatTime, formatTime2
from src.helpers.category import categorize_time
from models.train import append_new_record, train_model
from models.train2 import append_new_record2, train_model2
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

def train1(body: trainBody):
    df = pd.DataFrame([body.dict()])
    print("appending")
    append_new_record(df)
    print("training")
    # train_model()
    return {"success": True}

def train2(body: trainBody2):
    data = transform_input(body)
    df = pd.DataFrame([data])
    append_new_record2(df)
    # train_model2()
    return {"success": True}