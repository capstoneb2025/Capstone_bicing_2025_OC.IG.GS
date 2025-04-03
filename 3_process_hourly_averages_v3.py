import pandas as pd
import numpy as np
import os
from pathlib import Path

time_way=1

def process_hourly_averages(input_folder):
    """
    Process all CSV files in subfolders containing hourly data and create averaged versions.
    
    Args:
        input_folder (str): Path to the root folder containing subfolders with CSV files
    """
    # Define dtypes for faster reading and less memory usage
    dtypes = {
        'station_id': 'Int32',
        'num_bikes_available': 'Int32',
        'num_bikes_available_types.mechanical': 'Int32',
        'num_bikes_available_types.ebike': 'Int32',
        'num_docks_available': 'Int32',
        'is_installed': 'boolean',
        'is_renting': 'boolean',
        'is_returning': 'boolean',
        'last_reported': 'Int64',
        'is_charging_station': 'boolean',
        'status': 'string',
        'last_updated': 'Int64',
        'ttl': 'Int32'
    }
    # Find all CSV files in subfolders
    csv_files = list(Path(input_folder).rglob("*.csv")) 
        
    print(f"\nFound {len(csv_files)} matching CSV files:")
    for file in csv_files:
        print(f"- {file.name}")
    print()  # Empty line for readability

    for file in csv_files:
        try:
            print(f"Processing: {file}...")
            
            # Create output filename
            output_file = file.parent / f"{file.stem}_averaged{file.suffix}"
            
            # Skip if output file already exists
            if output_file.exists():
                print(f"Skipping: {output_file} already exists")
                continue
            
            # Read CSV file
            df = pd.read_csv(file, dtype=dtypes, low_memory=False)
            
            print(f"Rows before dropping NaN values: {len(df)}")

            # Drop rows containing any NaN values
            df = df.dropna(subset=['last_reported'])

            print(f"Rows after dropping last_reported values: {len(df)}")

            # Drop rows containing spurious values
            df = df[
                (df["is_installed"] != 0) & 
                (df["is_renting"] != 0) & 
                (df["is_returning"] != 0) & 
                (df["is_charging_station"] != False) & 
                (df["status"] == "IN_SERVICE")
                ]
            
            print(f"Rows after dropping spurious NaN values: {len(df)}")

            # Drop non-used columns
            print(f"Original columns: {df.columns}")

            df = df[['station_id', 'num_docks_available', 'last_reported']]

            print(f"Final columns: {df.columns}")

            # Convert timestamps
            # Convert last_reported to datetime first
            df['datetime'] = pd.to_datetime(df['last_reported'], unit='s', utc=True)
            # Extract date components from the converted datetime column
            df['year'] = df['datetime'].dt.year
            df['month'] = df['datetime'].dt.month
            df['day'] = df['datetime'].dt.day
            df['hour'] = df['datetime'].dt.hour
                        
            # Create date column without time component
            df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
                        
                  
           
            # Group by station and hour, then aggregate
            result_df = df.groupby(['station_id', 'year', 'month', 'day', 'hour', 'date'])['num_docks_available'].mean().reset_index()
            
            # Save to new CSV file
            result_df.to_csv(output_file, index=False)
            print(f"Created: {output_file}")
            
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")

if __name__ == "__main__":
    # Example usage
    input_folder = r"E:\data\unzipped"
    process_hourly_averages(input_folder) 