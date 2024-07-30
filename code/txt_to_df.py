import os
import shutil
from os import getcwd
import pandas as pd

def move_txt_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Debugging: Confirm the paths
    print(f"Source folder: {source_folder}")
    print(f"Destination folder: {destination_folder}")

    for subdir, _, files in os.walk(source_folder):
        # Debugging: Confirm each subdirectory being processed
        print(f"Processing directory: {subdir}")

        for file in files:
            if file.endswith('.txt'):
                source_path = os.path.join(subdir, file)
                destination_path = os.path.join(destination_folder, file)

                # Debugging: Confirm each file found
                print(f"Found txt file: {source_path}")

                # If a file with the same name already exists in the destination, rename it
                if os.path.exists(destination_path):
                    base, extension = os.path.splitext(file)
                    counter = 1
                    new_destination_path = os.path.join(destination_folder, f"{base}_{counter}{extension}")
                    while os.path.exists(new_destination_path):
                        counter += 1
                        new_destination_path = os.path.join(destination_folder, f"{base}_{counter}{extension}")
                    destination_path = new_destination_path

                shutil.move(source_path, destination_path)
                # Debugging: Confirm each move operation
                print(f"Moved: {source_path} -> {destination_path}")


source_folder = getcwd() + '/data/tcga_data'
destination_folder = getcwd() + '/data/processed'  # Replace with the desired output folder path

move_txt_files(source_folder, destination_folder)

txts_path = getcwd() + '/data/processed/tcga_methyl_processed'
count = 0
for name in os.listdir(txts_path):
    temp_file_path = f'{txts_path}/{name}'
    df = pd.read_csv(temp_file_path, names=['site', 'beta_val'], sep='	')
    count += 1
    df.to_csv(f'{getcwd()}/data/processed/methyl_dfs/df{count}.csv')
print(count)
