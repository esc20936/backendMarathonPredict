import pandas as pd

# Cargar los archivos CSV
data = pd.read_csv(
    "../data2/Berlin_Marathon_data_1974_2019.csv",
    low_memory=False
)
data_weather = pd.read_csv(
    "../data2/Berlin_Marathon_weather_data_since_1974.csv",
    low_memory=False
)

# Eliminar filas con valores nulos o inválidos en la columna 'TIME'
filtered_data = data.dropna(subset=['TIME'])
filtered_data = filtered_data[filtered_data['TIME'] != "no time"]

# Convertir 'TIME' a segundos totales
filtered_data['TIME'] = pd.to_timedelta(filtered_data['TIME']).dt.total_seconds()

# Actualizar el dataset original con los datos filtrados
data = filtered_data

# Combinar los datasets en base a la columna 'YEAR'
combined_data = pd.merge(data, data_weather, on='YEAR', how='inner')

# Convertir la columna 'AGE' a numérica y eliminar filas con valores nulos en 'AGE'
combined_data['AGE'] = pd.to_numeric(combined_data['AGE'], errors='coerce')
combined_data = combined_data.dropna(subset=['AGE'])

# Guardar los datos combinados en un archivo CSV
output_file_path = "./data_model2.csv"
combined_data.to_csv(output_file_path, index=False)