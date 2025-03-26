### CAPSTONE_BICING_2025



import pandas as pd
import numpy as np
from lightgbm import LGBMRegressor
from lightgbm import early_stopping
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

from my_functions import check_nan_values, extract_time_components, show_nan_rows, get_unique_values_with_nan, merge_station_info, compare_df_cols, day_of_week, last_reported, convert_object_columns_to_boolean, convert_object_columns_to_category

# Load the data
df = pd.read_csv('data/Bicing_data_merged_3.csv')
# Read the metadata sample submission
sample = pd.read_csv('sample/metadata_sample_submission_2025.csv')
# Read station capacity information
stations_info = pd.read_csv('data\Informacio_estacions_bicing_2025.csv')

# Filter df to only include stations that are in the sample submission
# Calculate and print percentage of rows removed
original_rows = len(df)
df = df[df['station_id'].isin(sample['station_id'].unique())]
remaining_rows = len(df)
pct_removed = ((original_rows - remaining_rows) / original_rows) * 100

print(f"Removed {pct_removed:.2f}% of rows")

time_column = 'last_reported'

# Convert last_reported to datetime
df[time_column] = pd.to_datetime(df[time_column])

# Fill missing altitude values for specific stations
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

# Calculate percentage of docks available
df['percentage_docks_available'] = (df['num_docks_available'] / df['capacity'] ).round(2)

df_2 = df.copy()

Feature engineering


columns_to_lag_linear = ['percentage_docks_available'] #WEATHER, FESTIU
columns_to_lag_bfill = ['status']
df=create_lags(df, df, columns_to_lag_linear, columns_to_lag_bfill=columns_to_lag_bfill, time_column='last_reported')

Adapt Metadata for equal format

rom my_functions import print_unique_values

# Print unique values for columns with less than 10 unique values
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

# Merge station info
sample = merge_station_info(sample)

# Create a mapping for ctx-1, ctx-2, ..., ctx-4 to the new names
column_mapping = {
    'ctx-1': 'lag_1h_percentage_docks_available',
    'ctx-2': 'lag_2h_percentage_docks_available',
    'ctx-3': 'lag_3h_percentage_docks_available',
    'ctx-4': 'lag_4h_percentage_docks_available'
}

# Use the mapping to rename the columns
sample = sample.rename(columns=column_mapping)

# Add year
sample['year']=2024
day_of_week(sample)
last_reported(sample)
sample[['status','lag_1h_status', 'lag_2h_status', 'lag_3h_status', 'lag_4h_status' ]]='IN_SERVICE'
sample[['lag_1h_is_interpolated','lag_2h_is_interpolated','lag_3h_is_interpolated','lag_4h_is_interpolated']]= False
# Assuming 'sample' is your DataFrame
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

Model

# df = df[df['year']>2022]

# Define train, validation, and test splits based on time
# Using 70% for training, 15% for validation, and 15% for testing
train_end = df[time_column].quantile(0.7)
val_end = df[time_column].quantile(0.85)

train_data = df[df[time_column] <= train_end]
val_data = df[(df[time_column] > train_end) & (df[time_column] <= val_end)]
test_data = df[df[time_column] > val_end]

# # Handle categorical variables
# le = LabelEncoder()
# for col in ['station_id']:
#     df[col] = le.fit_transform(df[col])

# Split features and target
X_train = train_data[feature_columns]
y_train = train_data[target_column]
X_val = val_data[feature_columns]
y_val = val_data[target_column]
X_test = test_data[feature_columns]
y_test = test_data[target_column]

# Initialize and train the model
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


# Make predictions
train_pred = model.predict(X_train)
val_pred = model.predict(X_val)
test_pred = model.predict(X_test)

# Evaluate the model
print("\nModel Performance:")
print("Training R2 Score:", r2_score(y_train, train_pred))
print("Validation R2 Score:", r2_score(y_val, val_pred))
print("Test R2 Score:", r2_score(y_test, test_pred))

print("\nRMSE Scores:")
print("Training RMSE:", np.sqrt(mean_squared_error(y_train, train_pred)))
print("Validation RMSE:", np.sqrt(mean_squared_error(y_val, val_pred)))
print("Test RMSE:", np.sqrt(mean_squared_error(y_test, test_pred)))

# Feature importance
feature_importance = pd.DataFrame({
    'feature': feature_columns,
    'importance': model.feature_importances_
})
print("\nFeature Importance:")
print(feature_importance.sort_values('importance', ascending=False))

# Combine train and validation data for final training
X_full = pd.concat([X_train, X_val])
y_full = pd.concat([y_train, y_val])

# Train final model on full training data
final_model = LGBMRegressor(
    n_estimators=model.best_iteration_,  # Use best iteration from validation
    learning_rate=0.1,
    random_state=42
)

final_model.fit(X_full, y_full)

# Evaluate on test set
test_pred_final = final_model.predict(X_test)
print("\nFinal Model Test Performance:")
print("Test R2 Score:", r2_score(y_test, test_pred_final))
print("Test RMSE:", np.sqrt(mean_squared_error(y_test, test_pred_final)))

# Update model reference for predictions
model = final_model

# Reorder the columns of prediction_data to match X_train's column order
prediction_data = sample[X_train.columns]

# Check if the columns of prediction_data match the columns of X_train
columns_match = prediction_data.columns.tolist() == X_train.columns.tolist()

# Print if the columns match
print("Columns match:", columns_match)

# If the columns don't match, print the differences
if not columns_match:
    print("Columns in prediction_data that are not in X_train:", set(prediction_data.columns) - set(X_train.columns))
    print("Columns in X_train that are not in prediction_data:", set(X_train.columns) - set(prediction_data.columns))

# Make predictions
predictions = model.predict(prediction_data)

# Print or further process predictions
print("Predictions:", predictions)

# Create final submission dataframe
final_submission = pd.DataFrame({'percentage_docks_available': predictions})

# Adding index column to final submission, starting at 0
final_submission['index'] = range(len(final_submission))

# Reorder columns to put index first
final_submission = final_submission[['index', 'percentage_docks_available']]

# Save the final submission with incremented suffix
# Get existing files matching pattern
import glob
existing_files = glob.glob('model_2/Sub_model_2_plain_*.csv')

# Extract existing numbers and find max
import re
numbers = [int(re.search(r'plain_(\d+)', f).group(1)) for f in existing_files if re.search(r'plain_(\d+)', f)]
next_num = max(numbers) + 1 if numbers else 1

output_file = f'model_2/Sub_model_2_plain_{next_num}.csv'
print(f"\nSaving final submission to: {output_file}")
final_submission.to_csv(output_file, index=False)
