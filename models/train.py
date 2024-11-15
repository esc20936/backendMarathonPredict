import pandas as pd
import numpy as np
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Función para agregar un nuevo registro y actualizar el archivo
def append_new_record(new_data_df, file_path="../data/external/MarathonData.csv"):
    """
    Agrega un nuevo registro desde un DataFrame al archivo existente y guarda los cambios.
    
    Args:
    new_data_df (pd.DataFrame): DataFrame con los nuevos registros a agregar.
    file_path (str): Ruta del archivo CSV existente. Por defecto es "../data/external/MarathonData.csv".
    """
    # Leer el archivo existente
    existing_df = pd.read_csv(file_path)
    
    # Verificar que las columnas coincidan entre el DataFrame existente y el nuevo
    if not set(new_data_df.columns).issubset(set(existing_df.columns)):
        raise ValueError("Las columnas del nuevo DataFrame no coinciden con las del archivo existente.")
    
    # Agregar los nuevos registros al archivo existente
    updated_df = pd.concat([existing_df, new_data_df], ignore_index=True)
    
    # Guardar el archivo actualizado
    updated_df.to_csv(file_path, index=False)

# Función para entrenar el modelo con la data actualizada
def train_model(file_path="'../data/external/MarathonData.csv'", model_path="marathon_model.joblib"):
    """
    Entrena un modelo con los datos del archivo actualizado y guarda el modelo entrenado.
    
    Args:
    file_path (str): Ruta del archivo CSV con los datos de entrenamiento.
    model_path (str): Ruta donde se guardará el modelo entrenado.
    """
    # Leer los datos
    df = pd.read_csv(file_path)
    
    # Convertir todos los valores a float
    df = df.apply(pd.to_numeric, errors='coerce')
    
    # Marcar las filas con 'CrossTraining' como 1, de lo contrario 0
    df['cross_training'] = np.where(df['CrossTraining'].notnull(), 1, 0)
    
    # Eliminar filas con 'Wall21' nulo
    df = df.dropna(subset=['Wall21'])
    
    # Separar características y objetivo
    y = df['MarathonTime']
    X = df[['cross_training', 'km4week', 'sp4week']]
    
    # Dividir los datos en conjuntos de entrenamiento y validación
    train_X, val_X, train_y, val_y = train_test_split(X, y)
    
    # Entrenar el modelo
    forest_model = RandomForestRegressor(random_state=1)
    forest_model.fit(train_X, train_y)
    
    # Guardar el modelo entrenado
    dump(forest_model, model_path)
    print(f"Modelo entrenado y guardado en: {model_path}")