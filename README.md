# CAPSTONE_BICING_2025

## Introduccció:

Como usuarios de Bicing y residentes de Barcelona, debatimos sobre qué variables incluir en el modelo para mejorarlo e incorporar la mayoría de los casos y situaciones que pueden favorecer o dificultar el uso del servicio de Bicing en la ciudad.
Escojimos 3 variables que respresentavan la mayoria de casuisticas significativas. Son la siguientes:

Variables climáticas:
Para ello, consideramos datos meteorológicos provenientes de la Xarxa d'Estacions Meteorològiques Automàtiques (XEMA) de la estación del Raval:
Temperatura
Precipitación máxima en 1 minuto
Dirección de la racha máxima del viento a 10 m
Velocidad del viento a 10 m (esc.)
Irradiancia solar global
Racha máxima del viento a 10 m
Precipitación
Humedad relativa

Eventos
Partidos del F.C. Barcelona: Utilizamos los datos de la web Livefutbol.com.

Festividades: Recurriendo a la web de Betevé del Ajuntament de Barcelona.

Para verificar la relevancia de estas variables, analizamos su impacto en la predicción mediante la creación de gráficos y mapas, ajustando las fechas y comparando los resultados con los datos reales. También identificamos fechas clave para evaluar si permitían predecir escenarios específicos, lo que ayudó a validar el modelo.
Para relizar el trabajo anterior de forma mas fluida usamos mtflow para comparar los efectos de las variaciones incorporadas.

Finalmente, consideramos que sería una buena idea aplicar el modelo en una aplicación, permitiendo sintetizar el trabajo en un sistema tangible.




Poner graficos barcelona estan incluidos los partidos locales i fuera de casa se nota que el cam nou esta de obras. i estan haciento los partidos en monjuic.

Aplicacion app ponder capturas de como funciona. predicciones con pardido del barça o sin partido 

Explicacion de coodigo:


## Explicación de las varibles extra incluidas en el modelo:

Se han incluido en el dataset las siguientes variables:

Variable lluvia: se ha incluido en el dataset una variable que registra las precipitaciones en Barcelona. Se analiza la primera hora que llueve. Con precipitaciones de mas de 1ml. I con los dias de no lluvia se identifica los dias en que no hay lluvia.

Variable partidos FCB: se ha incluido una variable que recoge todos los partidos del FC Barcelona, tanto en Barcelona como fuera.

En los siguientes gráficos, se puede observar cómo el uso de la variable lluvia (“si se registran precipitaciones”) tiene efectos positivos en la predicción del modelo. En cambio, si no hay la variable lluvia, la predicción también funciona correctamente però no tanto.
En los siguentes 2 graficos se pueden observar en dos fechas diferentes como en el momento en el que hay precipitaciones se reduce el percetage de dots disponobles
![Image](https://github.com/user-attachments/assets/565609d4-e185-422f-976e-22128347d6ec) 
![Image](https://github.com/user-attachments/assets/7692986e-08d9-4a03-b33f-1ab86c11f8b8) efecto sin lluvia
![Image](https://github.com/user-attachments/assets/5e0ab0f3-19c3-450f-aa4a-64b73a3ff567) efecte sol
![Image](https://github.com/user-attachments/assets/7d679508-db92-4a16-8dcb-66340f57f9e2) real juliol sense sol 

![Image](https://github.com/user-attachments/assets/11284f97-ea93-4b39-9f4f-98f3fa9e4de8) real 2020 juliol amb sol

![Image](https://github.com/user-attachments/assets/608de8d6-ad04-4580-a862-b87aa8f2e955) diferencia sol sense













![Image](https://github.com/user-attachments/assets/0dc15f32-5263-467f-9dcb-e14aca3770ae)


También se puede observar cómo, en el momento en que se produce la lluvia, el modelo predice correctamente que hay más spots de Bicing y mayor disponibilidad de bicicletas.

![Image](https://github.com/user-attachments/assets/5ea1a140-7709-41cd-b587-e229a28d7926)


Por otro lado, también se puede observar que en la zona de Plaça Espanya, donde actualmente se encuentran las conexiones de bus, metro y tren con el Bicing, así como la proximidad al estadio del FCB, el modelo funciona favorablemente.

En el momento en que se está disputando un partido en casa, se registra una disminución en la disponibilidad de bicicletas antes y durante el partido. Sin embargo, después del encuentro, la disponibilidad vuelve a aumentar.

Esta dinámica es bastante habitual debido a las diversas dificultades ocasionadas por la gran afluencia de aficionados que utilizan los servicios públicos para llegar al estadio.

![Image](https://github.com/user-attachments/assets/d6002146-b23c-49b8-a8ac-e02e4ea0edcc)


La predicción en todas las estaciones de Barcelona varía, aumentando la disponibilidad de bicicletas durante el partido y reduciéndose en las horas previas al encuentro.

![Image](https://github.com/user-attachments/assets/a5bcf9ae-24f3-4340-b3db-9a5d9097c492)



![Image](https://github.com/user-attachments/assets/e9aed01a-b223-40a5-8a1f-694e03238404)

![Image](https://github.com/user-attachments/assets/7ee606d8-67a6-4ce6-905f-3ae417df3d28) real partits gener 2020

![Image](https://github.com/user-attachments/assets/73123f8a-04dc-42d4-be1b-caa58bfad1e8) real gener 2020 sens ebara

![Image](https://github.com/user-attachments/assets/f02225bd-8004-454e-9c40-c62ad77a653a) prediccio fggener 2020

![Image](https://github.com/user-attachments/assets/1e8afcd0-bec7-452b-8205-4cb974ddadfd) predicció març 2024 20h


Tenemos version local y version en colab con ftflow explicar las diferencias.

Aplicacion Orlando

Conclusion:




# Explicacion de coodigo:

### Este código importa las librerías necesarias para trabajar con datos y entrenar un modelo de Machine Learning.
### Importamos numpy para cálculos numéricos y manejo de arrays. LightGBM, una librería eficiente para modelos de Gradient Boosting. Métricas para evaluar el rendimiento del modelo y LabelEncoder para convertir datos categóricos en números.
 
import pandas as pd
import numpy as np
from lightgbm import LGBMRegressor
from lightgbm import early_stopping
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

#### Importamos funciones personalizadas: check_nan_values para verificar valores NaN, extract_time_components para extraer componentes de tiempo, show_nan_rows para mostrar filas con valores NaN, get_unique_values_with_nan para obtener valores únicos incluyendo NaN, merge_station_info para fusionar información de estaciones, compare_df_cols para comparar columnas de DataFrames, day_of_week para obtener el día de la semana, last_reported para identificar el último reporte, convert_object_columns_to_boolean para convertir columnas tipo objeto a booleano y convert_object_columns_to_category para convertirlas a categoría. 

from my_functions import check_nan_values, extract_time_components, show_nan_rows, get_unique_values_with_nan, merge_station_info, compare_df_cols, day_of_week, last_reported, convert_object_columns_to_boolean, convert_object_columns_to_category

#### Cargamos un archivo CSV en un DataFrame utilizando pandas.

df = pd.read_csv('data/Bicing_data_merged_3.csv')

#### Cargamos un archivo CSV de muestra en un DataFrame

sample = pd.read_csv('sample/metadata_sample_submission_2025.csv')


#### Cargamos el archivo CSV con información de las estaciones de Bicing

stations_info = pd.read_csv('data\Informacio_estacions_bicing_2025.csv')

#### Guardamos el número de filas originales del DataFrame. Filtramos `df` para mantener solo las filas donde 'station_id' está en `sample`.  Contamos las filas restantes después del filtrado.  Calculamos el porcentaje de filas eliminadas y lo mostramos en pantalla. Y definimos la variable `time_column` con el nombre de la columna de tiempo.  

original_rows = len(df)
df = df[df['station_id'].isin(sample['station_id'].unique())]
remaining_rows = len(df)
pct_removed = ((original_rows - remaining_rows) / original_rows) * 100

print(f"Removed {pct_removed:.2f}% of rows")

time_column = 'last_reported'

#### Convertimos la columna de tiempo a formato datetime para facilitar su manipulación y análisis.

df[time_column] = pd.to_datetime(df[time_column])


#### Corregimos valores de altitud faltantes de estacions esos datos. Actualizamos la columna 'altitude' en `stations_info` usando el mapeo definido. Llamamos a `merge_station_info(df)` para fusionar información de estaciones con el DataFrame principal y llamamos a `check_nan_values(df)` para verificar la presencia de valores NaN en el DataFrame.  

altitude_mapping = {
    11: 6,
    271: 27,
    350: 43,
    381: 11
}

stations_info.loc[stations_info['station_id'].isin(altitude_mapping.keys()), 'altitude'] = \
    stations_info.loc[stations_info['station_id'].isin(altitude_mapping.keys()), 'station_id'].map(altitude_mapping)


merge_station_info(df)

check_nan_values(df)

#### Calculamos el porcentaje de docks disponibles dividiendo 'num_docks_available' por 'capacity' y redondeamos a 2 decimales. Creamos una copia del DataFrame original para futuras modificaciones.  

#### Feature engineering  
#### Definimos las columnas a las que aplicaremos retardos lineales ('percentage_docks_available').  Definimos las columnas a las que aplicaremos retardos con rellenado hacia adelante ('status'). Aplicamos la función `create_lags` para generar estas nuevas características en el DataFrame. Adaptamos los metadatos para mantener un formato uniforme.  Y importamos `print_unique_values` desde `my_functions` para mostrar valores únicos en el DataFrame.  

df['percentage_docks_available'] = (df['num_docks_available'] / df['capacity'] ).round(2)

df_2 = df.copy()

Feature engineering


columns_to_lag_linear = ['percentage_docks_available'] #WEATHER, FESTIU
columns_to_lag_bfill = ['status']
df=create_lags(df, df, columns_to_lag_linear, columns_to_lag_bfill=columns_to_lag_bfill, time_column='last_reported')

Adapt Metadata for equal format

rom my_functions import print_unique_values


#### Mostramos los valores únicos en las columnas de `df` con `print_unique_values(df)`. Comparamos las columnas de `df` y `sample` usando `compare_df_cols(df, sample)`. Creamos la función `day_of_week` para agregar la columna 'day_of_week' si no existe, calculándola a partir de las columnas de fecha y hora.  

print_unique_values(df)

compare_df_cols(df, sample)

def day_of_week (df):
    if ('day_of_week' in df.columns):
        print("day_of_week exist, skipping")
    else:
        # Add day_of_week based on date
        df['day_of_week'] = pd.to_datetime(
            df['year'].astype(str) + '-' + df['month'].astype(str) + '-' +
            df['day'].astype(str) + ' ' +
            df['hour'].astype(str) + ':00:00'
        ).dt.dayofweek

#### Merge station info
sample = merge_station_info(sample)

#### Creamos un diccionario `column_mapping` para mapear nombres de columnas con sus respectivos nombres modificados para los retardos de 1 a 4 horas (ctx-1, ctx-2, ..., ctx-4).  
column_mapping = {
    'ctx-1': 'lag_1h_percentage_docks_available',
    'ctx-2': 'lag_2h_percentage_docks_available',
    'ctx-3': 'lag_3h_percentage_docks_available',
    'ctx-4': 'lag_4h_percentage_docks_available'
}

#### Renombramos las columnas de `sample` utilizando el diccionario `column_mapping`.  
sample = sample.rename(columns=column_mapping)

#### Asignamos el valor 2024 a la columna 'year' de `sample`.  Llamamos a `day_of_week(sample)` y `last_reported(sample)` y Establecemos 'IN_SERVICE' en las columnas de estado y False en las columnas de interpolación.  

sample['year']=2024
day_of_week(sample)
last_reported(sample)
sample[['status','lag_1h_status', 'lag_2h_status', 'lag_3h_status', 'lag_4h_status' ]]='IN_SERVICE'
sample[['lag_1h_is_interpolated','lag_2h_is_interpolated','lag_3h_is_interpolated','lag_4h_is_interpolated']]= False

#### Asignamos True a las columnas de estado en `sample`. Mostramos los valores únicos de la columna 'status' en `df`. Comparamos las columnas de `df` y `sample`. Definimos las columnas de características y la columna objetivo . Y Convertimos columnas de objeto a booleano y a categoría en `df` y `sample`.

sample[['is_charging_station', 'is_installed', 'is_renting', 'is_returning']] = True


df['status'].unique()

compare_df_cols(df, sample)

feature_columns = ['altitude', 'capacity', 'day', 'day_of_week', 'hour', 'is_charging_station', 'is_installed', 'is_renting', 'is_returning', 'lag_1h_is_interpolated',
                'lag_1h_percentage_docks_available', 'lag_1h_status', 'lag_2h_is_interpolated', 'lag_2h_percentage_docks_available', 'lag_2h_status', 'lag_3h_is_interpolated',
                'lag_3h_percentage_docks_available', 'lag_3h_status', 'lag_4h_is_interpolated', 'lag_4h_percentage_docks_available', 'lag_4h_status',
                 'lat', 'lon', 'month', 'post_code', 'station_id', 'status', 'year']
target_column = 'percentage_docks_available'


convert_object_columns_to_boolean(df)
convert_object_columns_to_boolean(sample)

convert_object_columns_to_category(df)
convert_object_columns_to_category(sample)

# Model
#### Filtramos `df` para mantener solo las filas donde el año sea mayor a 2022.  

#### df = df[df['year']>2022]

#### Definimos el punto final para el conjunto de entrenamiento (70% de los datos).  Definimos el punto final para el conjunto de validación (85% de los datos). Y dividimos el DataFrame en tres conjuntos: entrenamiento, validación y prueba.

train_end = df[time_column].quantile(0.7)
val_end = df[time_column].quantile(0.85)

train_data = df[df[time_column] <= train_end]
val_data = df[(df[time_column] > train_end) & (df[time_column] <= val_end)]
test_data = df[df[time_column] > val_end]

### Asignamos las características y la columna objetivo para los conjuntos de entrenamiento, validación y prueba.  
X_train = train_data[feature_columns]
y_train = train_data[target_column]
X_val = val_data[feature_columns]
y_val = val_data[target_column]
X_test = test_data[feature_columns]
y_test = test_data[target_column]

#### Creamos un modelo `LGBMRegressor` con 1000 estimadores, una tasa de aprendizaje de 0.03 y una semilla aleatoria de 42. Y  entrenamos el modelo con los datos de entrenamiento y validación, utilizando 'rmse' como métrica y early stopping para evitar el sobreajuste.  

model = LGBMRegressor(
    n_estimators=1000,
    learning_rate=0.03,
    random_state=42
)

model.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    eval_metric='rmse',
    callbacks=[early_stopping(stopping_rounds=10, verbose=True)]
)


#### Realizamos predicciones sobre los conjuntos de entrenamiento, validación y prueba usando el modelo entrenado.  

train_pred = model.predict(X_train)
val_pred = model.predict(X_val)
test_pred = model.predict(X_test)

#### Evaluamos el modelo imprimiendo el R2 y RMSE para los conjuntos de entrenamiento, validación y prueba.  
print("\nModel Performance:")
print("Training R2 Score:", r2_score(y_train, train_pred))
print("Validation R2 Score:", r2_score(y_val, val_pred))
print("Test R2 Score:", r2_score(y_test, test_pred))

print("\nRMSE Scores:")
print("Training RMSE:", np.sqrt(mean_squared_error(y_train, train_pred)))
print("Validation RMSE:", np.sqrt(mean_squared_error(y_val, val_pred)))
print("Test RMSE:", np.sqrt(mean_squared_error(y_test, test_pred)))

#### Calculamos la importancia de las características y la mostramos ordenada de mayor a menor.  

feature_importance = pd.DataFrame({
    'feature': feature_columns,
    'importance': model.feature_importances_
})
print("\nFeature Importance:")
print(feature_importance.sort_values('importance', ascending=False))

#### Combinamos los datos de entrenamiento y validación para realizar el entrenamiento final del modelo.  

X_full = pd.concat([X_train, X_val])
y_full = pd.concat([y_train, y_val])

#### Entrenamos el modelo final usando los datos combinados de entrenamiento y validación, con el número óptimo de estimadores del modelo anterior.  

final_model = LGBMRegressor(
    n_estimators=model.best_iteration_,  # Use best iteration from validation
    learning_rate=0.1,
    random_state=42
)

final_model.fit(X_full, y_full)

#### Evaluamos el rendimiento del modelo final en el conjunto de prueba, calculando el R2 y RMSE.  

test_pred_final = final_model.predict(X_test)
print("\nFinal Model Test Performance:")
print("Test R2 Score:", r2_score(y_test, test_pred_final))
print("Test RMSE:", np.sqrt(mean_squared_error(y_test, test_pred_final)))

#### Actualizamos la referencia del modelo para usar el modelo final en futuras predicciones.  

model = final_model

#### Reordenamos las columnas de `prediction_data` para que coincidan con el orden de las columnas de `X_train`.  

prediction_data = sample[X_train.columns]

#### Comprobamos si las columnas de `prediction_data` coinciden con las columnas de `X_train`.  

columns_match = prediction_data.columns.tolist() == X_train.columns.tolist()

#### Imprimimos si las columnas de `prediction_data` coinciden con las de `X_train`.  

print("Columns match:", columns_match)

#### Si las columnas no coinciden, mostramos las diferencias entre las columnas de `prediction_data` y `X_train`.  

if not columns_match:
    print("Columns in prediction_data that are not in X_train:", set(prediction_data.columns) - set(X_train.columns))
    print("Columns in X_train that are not in prediction_data:", set(X_train.columns) - set(prediction_data.columns))

#### Realizamos predicciones utilizando el modelo final sobre los datos de `prediction_data`.  

predictions = model.predict(prediction_data)

#### Imprimimos las predicciones realizadas por el modelo.  

print("Predictions:", predictions)

#### Creamos el DataFrame final de envío con las predicciones para la columna 'percentage_docks_available'.  

final_submission = pd.DataFrame({'percentage_docks_available': predictions})

#### Agregamos una columna de índice al DataFrame final de envío, comenzando desde 0.  

final_submission['index'] = range(len(final_submission))

#### Reordenamos las columnas de `final_submission` para colocar la columna 'index' primero.  

final_submission = final_submission[['index', 'percentage_docks_available']]

#### Guardamos el archivo final con un sufijo incrementado. Y buscamos archivos existentes con el patrón 'model_2/Sub_model_2_plain_*.csv'.  

import glob
existing_files = glob.glob('model_2/Sub_model_2_plain_*.csv')

#### Extraemos el número máximo de los archivos existentes y le sumamos 1. Si no hay archivos previos, iniciamos con el número 1.  Y finalmente guardamos el archivo final

import re
numbers = [int(re.search(r'plain_(\d+)', f).group(1)) for f in existing_files if re.search(r'plain_(\d+)', f)]
next_num = max(numbers) + 1 if numbers else 1

output_file = f'model_2/Sub_model_2_plain_{next_num}.csv'
print(f"\nSaving final submission to: {output_file}")
final_submission.to_csv(output_file, index=False)


# Modelo 3:

