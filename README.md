# CAPSTONE_BICING_2025

## Introducción y desarrollo del proyecto:

Como usuarios de Bicing y residentes de Barcelona, debatimos sobre qué variables incluir en el modelo para mejorarlo e incorporar la mayoría de los casos y situaciones que pueden favorecer o dificultar el uso del servicio de Bicing en la ciudad.
Escojimos 3 variables que respresentavan la mayoria de casuisticas significativas. Son la siguientes:

-Variables climáticas:
Para ello, consideramos datos meteorológicos provenientes de la Xarxa d'Estacions Meteorològiques Automàtiques (XEMA) de la estación del Raval:
Temperatura
- Precipitación máxima en 1 minuto
- Dirección de la racha máxima del viento a 10 m
- Velocidad del viento a 10 m (esc.)
- Irradiancia solar global
- Racha máxima del viento a 10 m
- Precipitación
- Humedad relativa

Eventos
Partidos del F.C. Barcelona: Utilizamos los datos de la web Livefutbol.com.

Festividades: Recurriendo a la web de Betevé del Ajuntament de Barcelona.

Para verificar la relevancia de estas variables, analizamos su impacto mediante la creación de gráficos y mapas, ajustando las fechas y comparando los resultados con los datos reales y la predicción. También identificamos fechas clave para evaluar si permitían predecir escenarios específicos, lo que ayudó a validar el modelo.
Para relizar el trabajo anterior de forma mas fluida usamos mtflow para comparar los efectos de las variaciones incorporadas.

Finalmente, consideramos que sería una buena idea aplicar el modelo en una aplicación, permitiendo sintetizar el trabajo en un sistema tangible.

## Explicación de las varibles extra incluidas en el modelo:

Se han incluido en el dataset las siguientes variables:

Variable lluvia: se ha incluido en el dataset una variable que registra las precipitaciones en Barcelona. Se analiza la primera hora que llueve. Con precipitaciones de mas de 1ml. I con los dias de no lluvia se identifica los dias en que no hay lluvia.

Variable partidos FCB: se ha incluido una variable que recoge todos los partidos del FC Barcelona, tanto en Barcelona como fuera.

En los siguientes gráficos se puede observar cómo el uso de variables climáticas, como la lluvia (cuando se registran precipitaciones) y la radiación solar, tiene un impacto positivo en la predicción del modelo.

Asimismo, en los dos gráficos siguientes, correspondientes a fechas diferentes, se aprecia cómo el porcentaje de docks disponibles disminuye en el momento en que hay precipitaciones. Cuando comienza a llover, se evidencia que los usuarios depositan sus bicicletas en las estaciones.

![Image](https://github.com/user-attachments/assets/565609d4-e185-422f-976e-22128347d6ec) 

En los dos gráficos siguientes se observa cómo funciona la predicción cuando no hay lluvia. Este comportamiento muestra una tendencia muy similar al efecto de un día soleado, como se puede ver a continuación.

![Image](https://github.com/user-attachments/assets/7692986e-08d9-4a03-b33f-1ab86c11f8b8) 


En el siguiente gráfico se puede observar cómo funciona la variable "sol" en un día de julio. La radiación aumenta hasta el mediodía y luego comienza a descender hasta la puesta de sol.

![Image](https://github.com/user-attachments/assets/5e0ab0f3-19c3-450f-aa4a-64b73a3ff567)

En el siguiente gráfico se puede observar cómo aumenta el porcentaje de docks disponibles en un día de julio de 2020 sin sol. Se aprecia una menor disponibilidad en la zona costera.

![Image](https://github.com/user-attachments/assets/7d679508-db92-4a16-8dcb-66340f57f9e2) 

En el siguiente gráfico se puede observar un día de julio de 2020 con sol y cómo el porcentaje de docks disponibles aumenta significativamente, especialmente en la zona costera.

![Image](https://github.com/user-attachments/assets/11284f97-ea93-4b39-9f4f-98f3fa9e4de8) 

En el siguiente gráfico se puede observar la diferencia en el porcentaje de docks disponibles entre días soleados y días sin sol en un día de julio, evidenciando así su impacto.

![Image](https://github.com/user-attachments/assets/608de8d6-ad04-4580-a862-b87aa8f2e955) 



Variable "Eventos: Partidos del FC Barcelona"

Al incluir la variable "partido en casa", se observa cómo disminuye el porcentaje de docks disponibles alrededor del estadio donde se juega el partido.

En el siguiente gráfico se puede ver cómo, en la zona del Camp Nou, se produce una disminución en el porcentaje de docks disponibles en enero del 2020 a la hora del partido (20:00).

![Image](https://github.com/user-attachments/assets/7ee606d8-67a6-4ce6-905f-3ae417df3d28) 

Por otro lado, esta dinámica no se observa en días sin partido. Por ejemplo, en un día de enero de 2020, no se registra una disminución significativa en el porcentaje de docks disponibles alrededor del estadio.

![Image](https://github.com/user-attachments/assets/73123f8a-04dc-42d4-be1b-caa58bfad1e8) 



### Funcionamiento del modelo:

A continuacion vamos a mostra dos mapas de calor con la que creemos que se puede validar el la prediciones del modelo.

El siguiente mapa muestra la disponibilidad de docks predicha por el modelo en un día con partido en enero de 2020 a las 20:00 horas. Se puede observar cómo el modelo predice una disminución en la disponibilidad de docks en la zona del Camp Nou.
![Image](https://github.com/user-attachments/assets/f02225bd-8004-454e-9c40-c62ad77a653a) 


Por otro lado, también se observa una reducción predicha por el modelo en la disponibilidad de docks en la zona de Plaça Espanya durante un partido en marzo de 2024 a las 20:00 horas. Actualmente, esta área concentra conexiones de bus, metro y tren con el servicio de Bicing, facilitando el acceso al Estadio Lluís Companys, donde el FC Barcelona juega mientras el Camp Nou se encuentra en obras.

![Image](https://github.com/user-attachments/assets/1e8afcd0-bec7-452b-8205-4cb974ddadfd) 

En conclusión, basándonos en nuestro "sentido común", entendemos que estas predicciones tienen la capacidad de anticipar los comportamientos habituales de los usuarios del Bicing.
 
# Explicacion de codigo:

# Modelo 3 (definitivo):

!pip install mlflow streamlit pandas matplotlib scikit-learn joblib lightgbm

import pandas as pd
import numpy as np
from lightgbm import LGBMRegressor
from lightgbm import early_stopping
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

from google.colab import drive
drive.mount('/content/drive')

import sys
import os
#### Specify the root folder
root_folder = r'/content/drive/MyDrive/'

#### Walk through all subfolders and add them to sys.path
for root, dirs, files in os.walk(root_folder):
    sys.path.append(root)
import my_functions


from my_functions import check_nan_values, extract_time_components, show_nan_rows, get_unique_values_with_nan, merge_station_info, compare_df_cols, day_of_week, last_reported, convert_object_columns_to_boolean, convert_object_columns_to_category, create_lags, create_lag_lead, create_lag_lead_days, merge_barsa_data, merge_weather_data, merge_holiday_data, drop_non_time_column_dates, fill_na_holiday_columns


time_column='datetime'
feature_columns = ['station_id', 'month', 'day', 'hour',
       'lag_4h_percentage_docks_available',
       'lag_3h_percentage_docks_available',
       'lag_2h_percentage_docks_available',
       'lag_1h_percentage_docks_available', 'capacity', 'lat', 'lon',
       'altitude', 'post_code', 'year', 'day_of_week',
       'lag_1h_is_interpolated', 'lag_2h_is_interpolated',
       'lag_3h_is_interpolated', 'lag_4h_is_interpolated', 'FCB_Location',
       'FCB_Score', 'wea_prep', 'wea_sun', 'wea_temp', 'wea_wind_sp',
       'holiday', 'd_lag_1d_holiday',
       'd_lead_1d_holiday', 't_lag_1h_FCB_Location', 't_lag_1h_FCB_Score', 't_lag_1h_wea_prep',
       't_lag_1h_wea_sun', 't_lag_1h_wea_temp', 't_lag_1h_wea_wind_sp',
       't_lag_2h_FCB_Location', 't_lag_2h_FCB_Score', 't_lag_2h_wea_prep',
       't_lag_2h_wea_sun', 't_lag_2h_wea_temp', 't_lag_2h_wea_wind_sp',
       't_lag_3h_FCB_Location', 't_lag_3h_FCB_Score', 't_lag_3h_wea_prep',
       't_lag_3h_wea_sun', 't_lag_3h_wea_temp', 't_lag_3h_wea_wind_sp',
       't_lag_4h_FCB_Location', 't_lag_4h_FCB_Score', 't_lag_4h_wea_prep',
       't_lag_4h_wea_sun', 't_lag_4h_wea_temp', 't_lag_4h_wea_wind_sp',
       't_lead_1h_FCB_Location', 't_lead_1h_FCB_Score', 't_lead_1h_wea_prep',
       't_lead_1h_wea_sun', 't_lead_1h_wea_temp', 't_lead_1h_wea_wind_sp',
       't_lead_2h_FCB_Location', 't_lead_2h_FCB_Score', 't_lead_2h_wea_prep',
       't_lead_2h_wea_sun', 't_lead_2h_wea_temp', 't_lead_2h_wea_wind_sp',
       't_lead_3h_FCB_Location', 't_lead_3h_FCB_Score', 't_lead_3h_wea_prep',
       't_lead_3h_wea_sun', 't_lead_3h_wea_temp', 't_lead_3h_wea_wind_sp',
       't_lead_4h_FCB_Location', 't_lead_4h_FCB_Score', 't_lead_4h_wea_prep',
       't_lead_4h_wea_sun', 't_lead_4h_wea_temp', 't_lead_4h_wea_wind_sp']
target_column = 'percentage_docks_available'

#### Combine all columns into one list
selected_columns = feature_columns + [time_column] + [target_column]


# Load only the specified columns
df = pd.read_csv('/content/drive/MyDrive/Data/model_3/Train_prepared_v2.csv') #.sample(frac=frac_load, random_state=42)

df.info()


#### Convert last_reported to datetime
df[time_column] = pd.to_datetime(df[time_column])


convert_object_columns_to_boolean(df)


convert_object_columns_to_category(df)


df.info()

df['percentage_docks_available']

## Model
day_of_week(df)

#### Define train, validation, and test splits based on time
#### Using 70% for training, 15% for validation, and 15% for testing
train_end = df[time_column].quantile(0.7)

train_data = df[df[time_column] <= train_end]
val_data = df[df[time_column] > train_end]

import gc

del df  # Delete the DataFrame
gc.collect()  # Force garbage collection

#### Split features and target
X_train = train_data[feature_columns]
y_train = train_data[target_column]
X_val = val_data[feature_columns]
y_val = val_data[target_column]

!pip  install optuna

####  Imports for modeling
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import lightgbm as lgb
from lightgbm import LGBMRegressor
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform
import optuna

#### Create LightGBM datasets
train_data = lgb.Dataset(X_train, label=y_train, free_raw_data=True)
val_data = lgb.Dataset(X_val, label=y_val, reference=train_data, free_raw_data=True)

import lightgbm as lgb
import optuna
from sklearn.metrics import mean_squared_error

from sklearn.metrics import mean_squared_error
import numpy as np
#### Define the objective function for Optuna to optimize
def objective(trial):
    # Define the hyperparameter search space using Optuna
    params = {
        'objective': 'regression',  # Task type (regression)
        'metric': 'rmse',  # Evaluation metric (Root Mean Squared Error)
        'verbosity': -1,  # Suppress LightGBM logs
        'boosting_type': 'gbdt',  # Gradient Boosting Decision Trees
        'feature_pre_filter': False,  # No pre-filtering of features
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.5),  # Learning rate (between 0.01 and 0.3)
        'num_leaves': trial.suggest_int('num_leaves', 20, 1000),  # Maximum number of leaves per tree
        'max_depth': trial.suggest_int('max_depth', 3, 100),  # Maximum tree depth
        'min_data_in_leaf': trial.suggest_int('min_data_in_leaf', 10, 200),  # Minimum number of data in a leaf
        'feature_fraction': trial.suggest_float('feature_fraction', 0.8, 1.0),  # Fraction of features to use
        'bagging_fraction': trial.suggest_float('bagging_fraction', 0.8, 1.0),  # Fraction of data to use for bagging
        'bagging_freq': trial.suggest_int('bagging_freq', 1, 7),  # Frequency of bagging
    }

   #### Train the model with the given hyperparameters
    model = lgb.train(
        params,
        train_data,  # Training dataset
        valid_sets=[val_data],  # Validation dataset
        num_boost_round=1000,  # Maximum training rounds
        callbacks=[
            lgb.early_stopping(stopping_rounds=100),  # Stop early if no improvement
            lgb.log_evaluation(0)  # Log evaluation results
        ]
    )

    # Make predictions on the validation set
    preds = model.predict(X_val)

    # Calculate RMSE (Root Mean Squared Error)
    rmse = np.sqrt(mean_squared_error(y_val, preds))
    return rmse  # Return RMSE as the metric to minimize

# ========================
#### 2. Run Hyperparameter Tuning
# ========================

#### Create an Optuna study to minimize the RMSE
study = optuna.create_study(direction='minimize')

#### Run optimization for 10 trials
study.optimize(objective, n_trials=100)

#### Retrieve the best hyperparameters from the study
best_params = study.best_trial.params
print("Best Hyperparameters:", best_params)

#### ========================
#### 3. Train Final Model with Best Hyperparameters
#### ========================

#### Use the best parameters found during tuning
final_params = {
    'objective': 'regression',
    'metric': 'rmse',
    'verbosity': -1,
    'boosting_type': 'gbdt',
    **best_params  # Merge best hyperparameters into final parameters
}


#### Train the final model with the best hyperparameters
model = lgb.train(
    final_params,
    train_data,
    valid_sets=[val_data],
    num_boost_round=5000,  # Maximum training rounds
    callbacks=[
        lgb.early_stopping(stopping_rounds=100),  # Early stopping
        lgb.log_evaluation(50)  # Log evaluation results every 50 iterations
    ]
)

#### Save the trained model to a file
model.save_model('lightgbm_free_docks_model.txt')



#### Feature importance
feature_importance = pd.DataFrame({
    'feature': feature_columns,
    'importance': model.feature_importance(importance_type='gain')
})
print("\nFeature Importance:")
print(feature_importance.sort_values('importance', ascending=False))

#### feature_importance.sort_values('importance', ascending=False)

#### Train final model on combined train and validation data using best iteration
final_model = lgb.train(
    final_params,
    lgb.Dataset(pd.concat([X_train, X_val]), label=pd.concat([y_train, y_val])),
    num_boost_round=3052 #model.best_iteration  # Use best iteration from previous validation
)

#### Save the final model trained on combined data
final_model.save_model('lightgbm_free_docks_model_final.txt')

sample= pd.read_csv('data\Metadata_prepared_v2.csv')

convert_object_columns_to_boolean(sample)
convert_object_columns_to_category(sample)

#### Reorder the columns of prediction_data to match X_train's column order
prediction_data = sample[X_train.columns]


#### Check if the columns of prediction_data match the columns of X_train
columns_match = prediction_data.columns.tolist() == X_train.columns.tolist()

#### Print if the columns match
print("Columns match:", columns_match)

#### If the columns don't match, print the differences
if not columns_match:
    print("Columns in prediction_data that are not in X_train:", set(prediction_data.columns) - set(X_train.columns))
    print("Columns in X_train that are not in prediction_data:", set(X_train.columns) - set(prediction_data.columns))


    # Make predictions
predictions = final_model.predict(prediction_data)

#### Print or further process predictions
print("Predictions:", predictions)

#### Create final submission dataframe with explicit index
final_submission = pd.DataFrame({
    'index': range(len(predictions)),
    'percentage_docks_available': predictions
})

#### Create the directory if it doesn't exist
import os
os.makedirs('model_3', exist_ok=True)

#### Get existing files matching pattern
import glob
import re

existing_files = glob.glob('model_3/Sub_model_3_plain_*.csv')

#### Extract existing numbers and find max
numbers = [int(re.search(r'plain_(\d+)', f).group(1)) for f in existing_files if re.search(r'plain_(\d+)', f)]
next_num = max(numbers) + 1 if numbers else 1

#### Create final submission dataframe with explicit index and convert to numpy array first
submission_data = np.column_stack((np.arange(len(predictions)), predictions))
final_submission = pd.DataFrame(
    submission_data,
    columns=['index', 'percentage_docks_available']
).astype({'index': int, 'percentage_docks_available': float})

#### Save to CSV
output_file = f'model_3/Sub_model_3_plain_{next_num}.csv'
print(f"\nSaving final submission to: {output_file}")

#### Use numpy savetxt instead of pandas to_csv
np.savetxt(
    output_file,
    submission_data,
    delimiter=',',
    header='index,percentage_docks_available',
    comments='',
    fmt=['%d', '%.6f']
)

print(type(final_submission))  # Confirm it's a DataFrame
print(final_submission.dtypes)  # Check column data types
print(final_submission.columns)  # See column names
print(final_submission.index)  # Check index structure
print(final_submission.head())  # Preview data



# Modelo 2:

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

