import joblib

def loadModel():
    model = joblib.load('models/marathon_model.joblib')
    return model