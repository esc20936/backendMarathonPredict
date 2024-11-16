from src.schemas.predictBody import PredictBody2, trainBody2

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

def transform_input_train(data: trainBody2):
    # Convert GENDER to GENDER_male column as expected by the model
    gender_male = data.GENDER.lower() == 'male'
    
    # Create a dictionary with the transformed data
    transformed_data = {
        'AGE': data.AGE,
        'ATMOS_PRESS_mbar': data.ATMOS_PRESS_mbar,
        'AVG_TEMP_C': data.AVG_TEMP_C,
        'GENDER_male': gender_male,
        'time': data.time,
    }
    
    return transformed_data
