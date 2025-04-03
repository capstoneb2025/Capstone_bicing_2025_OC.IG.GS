import os
import pandas as pd
import glob
from pathlib import Path
import csv


def combine_csv_files_common_columns(folder_path, output_filename):
    """
    Combine all averaged CSV files, keeping only common columns.
    First loads all files, then processes and saves.
    """
    # Find all averaged CSV files in subfolders
    csv_files = [f for f in Path(folder_path).rglob("*.csv") 
                 if "_averaged" in f.stem]
    
    # Print number of files found
    print(f"\nFound {len(csv_files)} averaged CSV files:")
    for file in csv_files:
        print(f"- {file.name}")
    print()

    if not csv_files:
        print("No averaged CSV files found in the specified folder and subfolders.")
        return

    # Initialize list to store all dataframes
    all_dfs = []
    common_columns = None
    first_file_columns = None  # Store column order from first file
    
    # First pass: read files and determine common columns
    print("First pass: Reading files and determining common columns...")
    for file in csv_files:
        try:
            print(f"Reading: {file}")
            df = pd.read_csv(file, on_bad_lines='warn')
            
            if common_columns is None:
                common_columns = set(df.columns)
                first_file_columns = list(df.columns)  # Save column order from first file
            else:
                common_columns = common_columns.intersection(set(df.columns))
                
            all_dfs.append(df)
            print(f"Successfully read: {len(df)} rows")
        except Exception as e:
            print(f"Error reading {file}: {str(e)}")
    
    if not common_columns:
        print("No common columns found across CSV files.")
        return

    # Convert common_columns to list and use order from first file
    common_columns = list(common_columns)
    desired_order = [col for col in first_file_columns if col in common_columns]
    
    print(f"\nCommon columns (in order from first file): {desired_order}")
    
    # Process and combine all dataframes
    print("\nProcessing and combining data...")
    total_rows_initial = sum(len(df) for df in all_dfs)
    
    # Combine all dataframes
    combined_df = pd.concat(all_dfs, ignore_index=True)
    
    # Select only common columns and remove rows with any NaN values
    combined_df = combined_df[desired_order].dropna(how='any')
    
    # Remove any duplicate rows
    combined_df = combined_df.drop_duplicates()
    
    # Print statistics
    total_rows_final = len(combined_df)
    rows_removed = total_rows_initial - total_rows_final
    
    print(f"\nProcessing complete:")
    print(f"Initial total rows: {total_rows_initial}")
    print(f"Final total rows: {total_rows_final}")
    print(f"Rows removed: {rows_removed}")
    
    # Save the final dataframe
    print(f"\nSaving to {output_filename}...")
    combined_df.to_csv(output_filename, index=False)
    print("Save complete!")

if __name__ == "__main__":
    # Example usage
    folder_path = r"E:\data\unzipped"
    output_file = r"E:\data\capstone\Bicing_data_merged_5.csv"
    combine_csv_files_common_columns(folder_path, output_file)
