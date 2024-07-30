import os
import subprocess
from os import getcwd
import pandas as pd

# Path to gdc-client executable
gdc_client_path = getcwd() + '/data/manifests/gdc-client'

# Path to your manifest file
manifest_path = getcwd() + '/data/manifests/gdc_manifest.2024-07-30.txt'

# Function to download data using gdc-client
def download_data(gdc_client_path, manifest_path, output_dir):
    command = [gdc_client_path, 'download', '-m', manifest_path, '-d', output_dir]
    subprocess.run(command, check=True)

# Output directory for downloaded files
output_dir = 'tcga_data'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
print(output_dir)
# Download the data
download_data(gdc_client_path, manifest_path, output_dir)
print(getcwd())