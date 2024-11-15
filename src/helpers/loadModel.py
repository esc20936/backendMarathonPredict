import joblib

def loadModel(v2=False):
    path = {
        True: 'models/best_model_pipeline.joblib',
        False: 'models/marathon_model.joblib'
    }
    model = joblib.load(path[v2])
    return model
