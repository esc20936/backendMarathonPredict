import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn import tree
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

def append_new_record2(new_data_df, path="../data2/data_model2.csv"):
    """
    Agrega un nuevo registro desde un DataFrame al archivo existente y guarda los cambios.
    
    Args:
    new_data_df (pd.DataFrame): DataFrame con los nuevos registros a agregar.
    path (str): Ruta del archivo CSV existente. Valor por defecto es "../data2/data_model2.csv".
    """
    # Leer el archivo existente
    df = pd.read_csv(path)
    
    # Verificar que las columnas coincidan entre el DataFrame existente y el nuevo
    if not set(new_data_df.columns).issubset(set(df.columns)):
        raise ValueError("Las columnas del nuevo DataFrame no coinciden con las del archivo existente.")
    
    # Agregar los nuevos registros al archivo existente
    updated_df = pd.concat([df, new_data_df], ignore_index=True)
    
    # Guardar el archivo actualizado
    updated_df.to_csv(path, index=False)
    # print(f"Nuevo registro agregado al archivo: {path}")

def train_model2(path="../data2/data_model2.csv", model_path="best_model_pipeline.joblib"):
    """
    Entrena un modelo con los datos del archivo actualizado y guarda el modelo entrenado.
    
    Args:
    path (str): Ruta del archivo CSV con los datos de entrenamiento. Valor por defecto es "../data2/data_model2.csv".
    model_path (str): Ruta donde se guardará el modelo entrenado. Valor por defecto es "best_model_pipeline.joblib".
    """
    # Leer los datos
    combined_data = pd.read_csv(path)
    
    # Selección de columnas numéricas para la matriz de correlación
    numeric_data = combined_data.select_dtypes(include=[float, int])
    correlation_matrix = numeric_data.corr()  # Opcional si deseas visualizarlo
    
    # Preparar las características y el objetivo
    y = combined_data['TIME']
    X = combined_data[['GENDER', 'AGE', 'ATMOS_PRESS_mbar', 'AVG_TEMP_C']]
    X = pd.get_dummies(X, columns=['GENDER'], drop_first=True)
    
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Crear un pipeline
    pipeline = Pipeline([
        ('regr', LinearRegression())  # Modelo por defecto
    ])
    
    # Espacio de búsqueda para GridSearch
    search_space = [
        {'regr': [tree.DecisionTreeRegressor()], 
         'regr__max_depth': [None, 10, 20]}
    ]
    
    # Realizar GridSearch para encontrar el mejor modelo
    gs = GridSearchCV(pipeline, param_grid=search_space, scoring='neg_mean_squared_error', cv=5)
    gs.fit(X_train, y_train)
    
    # Evaluar el modelo en el conjunto de prueba
    y_pred = gs.best_estimator_.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print(f"Root Mean Squared Error en el conjunto de prueba: {rmse:.2f}")
    
    # Guardar el modelo entrenado
    joblib.dump(gs.best_estimator_, model_path)
    print(f"Modelo guardado en: {model_path}")