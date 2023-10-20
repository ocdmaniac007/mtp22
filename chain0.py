import os
import multiprocessing
from pathlib import Path
from tqdm import tqdm

def process_pdb_file(pdb_file, output_file):
    with open(pdb_file, 'r') as f:
        lines = f.readlines()

    # Check if any line in the PDB file has a chain ID of "0"
    has_chain_0 = any(line[21] == '0' for line in lines if line.startswith('ATOM'))

    if has_chain_0:
        with open(output_file, 'a') as output_txt:
            output_txt.write(f"{pdb_file.name}\n")

input_folder = "/home/mt0/22CS60R49/MTP/Chain_sep"
output_txt_file = "Chain_01_filenames.txt"

# Clear the content of the existing output file if it exists
if os.path.exists(output_txt_file):
    open(output_txt_file, 'w').close()

pdb_files = [Path(input_folder, filename) for filename in os.listdir(input_folder) if filename.endswith(".pdb")]

pool = multiprocessing.Pool()
progress_bar = tqdm(total=len(pdb_files), desc="Processing PDB files")

for pdb_file in pdb_files:
    pool.apply_async(process_pdb_file, args=(pdb_file, output_txt_file), callback=lambda _: progress_bar.update(1))

pool.close()
pool.join()
progress_bar.close()
