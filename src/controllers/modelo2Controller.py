from src.schemas.predictBody import PredictBody2
from src.helpers.loadModel import loadModel2
from src.helpers.formatTime import formatTime, formatTime2
from src.helpers.category import categorize_time
import pandas as pd

def transform_input(data: PredictBody2):
    # Convert GENDER to GENDER_male column as expected by the model
    gender_male = data.GENDER.lower() == 'male'
    
    # Create a dictionary with the transformed data
    transformed_data = {
        'AGE': data.AGE,
        'ATMOS_PRESS_mbar': data.ATMOS_PRESS_mbar,
        'AVG_TEMP_C': data.AVG_TEMP_C,
        'GENDER_male': gender_male
    }
    
    return transformed_data

def predict2(body: PredictBody2):
    input = transform_input(body)
    df = pd.DataFrame([input])
    print(df)
    model = loadModel2()
    prediction = model.predict(df)
    prediction = [round(prediction[0], 3)]
    time = formatTime2(prediction[0])
    category = categorize_time(prediction[0])
    return {"time": time}