import os
import multiprocessing
from pathlib import Path
import shutil
from tqdm import tqdm  # Import tqdm for the progress bar

# Define a function to split a PDB file into chains
def split_pdb_into_chains(pdb_file, output_folder):
    with open(pdb_file, 'r') as f:
        lines = f.readlines()

    chain_data = {}
    current_chain_id = None

    for line in lines:
        if line.startswith('ATOM'):
            chain_id = line[21]
            if current_chain_id is None or current_chain_id != chain_id:
                current_chain_id = chain_id
                chain_data[current_chain_id] = []
            chain_data[current_chain_id].append(line)

    for chain_id, data in chain_data.items():
        output_file = Path(output_folder, f"{pdb_file.stem}_{chain_id}.pdb")
        with open(output_file, 'w') as f:
            f.writelines(data)

# Specify the input folder containing PDB files and the output folder
input_folder = "/home/mt0/22CS60R49/MTP/downloaded_pdbs"
output_folder = "Chain_sep"

os.makedirs(output_folder, exist_ok=True)

# Get a list of all PDB files in the input folder
pdb_files = [Path(input_folder, filename) for filename in os.listdir(input_folder) if filename.endswith(".pdb")]

# Create a pool of worker processes
pool = multiprocessing.Pool()

# Create a tqdm progress bar for tracking the progress
progress_bar = tqdm(total=len(pdb_files), desc="Processing PDB files")

# Parallelize the computation for each PDB file
for pdb_file in pdb_files:
    pool.apply_async(split_pdb_into_chains, args=(pdb_file, output_folder), callback=lambda _: progress_bar.update(1))

# Close the pool and wait for the processes to finish
pool.close()
pool.join()

# Close the progress bar
progress_bar.close()
