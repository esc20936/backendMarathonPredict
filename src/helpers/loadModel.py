import joblib

def loadModel():
    model = joblib.load('models/marathon_model.joblib')
    return model

def loadModel2():
    model = joblib.load('models/best_model_pipeline.joblib')
    return model