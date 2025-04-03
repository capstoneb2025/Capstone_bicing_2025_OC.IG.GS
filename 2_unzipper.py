import os
import py7zr

def unzip_all_7z_files(folder_path):
    # Define the output directory
    output_dir = os.path.join(folder_path, "unzipped")
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate through all .7z files in the folder
    for file in os.listdir(folder_path):
        if file.endswith(".7z"):
            file_path = os.path.join(folder_path, file)
            extract_path = os.path.join(output_dir, os.path.splitext(file)[0])
            
            os.makedirs(extract_path, exist_ok=True)
            
            # Extract the .7z file
            with py7zr.SevenZipFile(file_path, mode='r') as archive:
                archive.extractall(path=extract_path)
                print(f"Extracted: {file} -> {extract_path}")

# Example usage
folder_path = r"E:\data"  # Change this to your target folder
unzip_all_7z_files(folder_path)