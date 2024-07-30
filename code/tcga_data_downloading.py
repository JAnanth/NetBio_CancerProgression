import os
import subprocess
import pandas as pd
from os import getcwd
# af
print(getcwd())

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
output_dir
# Download the data
download_data(gdc_client_path, manifest_path, output_dir)
