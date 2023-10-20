import os
import subprocess
from multiprocessing import Pool
from Bio.PDB import PDBParser
initial_file='3sxs_A_new.pdb'

# Path to the TM-align executable
tm_align_path = "/home/mt0/22CS60R49/MTP/TMalign"

# Input folder containing PDB files
input_folder = "/home/mt0/22CS60R49/MTP/pdb_with_atoms_only"

# Output folder to save TM-align results
output_folder = "tm_align_results"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Function to run TM-align for a pair of PDB files
def run_tm_align_parallel(args):
    pdb_file1, pdb_file2, output_file = args
    command = f"{tm_align_path} {pdb_file1} {pdb_file2} -a T > {output_file}"
    subprocess.run(command, shell=True, check=True)

# List all PDB files in the input folder
pdb_files = [file for file in os.listdir(input_folder) if file.endswith(".pdb")]

# Prepare arguments for parallel execution
args_list = [(initial_file, os.path.join(input_folder, pdb_file), os.path.join(output_folder, f"{initial_file}_{pdb_file}.tmalign"))
             for pdb_file in pdb_files]

# Set the number of processes to use (adjust according to your available CPU cores)
num_processes = 10

# Run TM-align in parallel
with Pool(num_processes) as pool:
    pool.map(run_tm_align_parallel, args_list)
