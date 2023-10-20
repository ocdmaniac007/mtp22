import os
import requests
from tqdm import tqdm
import multiprocessing

# Define the path to the text file containing PDB IDs
pdb_id_file = 'defects.txt'

# Define the base URL for RCSB PDB files
base_url = 'https://files.rcsb.org/view/'

# Function to download a PDB file given a PDB ID
def download_pdb(pdb_id, download_folder):
    pdb_url = f'{base_url}{pdb_id}.pdb'
    response = requests.get(pdb_url, stream=True)

    if response.status_code == 200:
        # Create the download folder if it doesn't exist
        os.makedirs(download_folder, exist_ok=True)

        # Save the PDB file with a progress bar
        pdb_filename = f'{pdb_id}.pdb'
        with open(os.path.join(download_folder, pdb_filename), 'wb') as pdb_file, tqdm(
            desc=f'Downloading {pdb_id}',
            total=int(response.headers.get('content-length', 0)),
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for data in response.iter_content(chunk_size=1024):
                pdb_file.write(data)
                pbar.update(len(data))
    else:
        print(f'Failed to download: {pdb_id}')

# Read the list of PDB IDs from the text file
with open(pdb_id_file, 'r') as file:
    pdb_ids = file.read().split()

# Specify the folder where downloaded PDB files will be saved
download_folder = 'downloaded_pdbs'

# Number of processes to use (adjust as needed)
num_processes = multiprocessing.cpu_count()

# Create a pool of worker processes
with multiprocessing.Pool(num_processes) as pool:
    # Create an overall progress bar
    overall_progress_bar = tqdm(total=len(pdb_ids), desc="Overall Progress")

    # Define a callback function to update the overall progress bar
    def update_progress(*_):
        overall_progress_bar.update()

    # Parallelize the downloading of PDB files
    for pdb_id in pdb_ids:
        pool.apply_async(download_pdb, args=(pdb_id, download_folder), callback=update_progress)

    # Close the pool and wait for the processes to finish
    pool.close()
    pool.join()

# Close the overall progress bar
overall_progress_bar.close()
