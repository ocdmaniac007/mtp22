import os
from pathlib import Path
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

def main(input_filename, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Check if the input file exists
    if not os.path.isfile(input_filename):
        print(f"Input file '{input_filename}' does not exist.")
        return

    # Split the PDB file into chains
    split_pdb_into_chains(input_filename, output_folder)

if __name__ == "__main__":
    # Specify the input PDB filename and the output folder
    input_pdb_filename = "your_input_pdb_file.pdb"  # Replace with your input filename
    output_folder = "Chain_sep"  # Replace with your output folder

    # Run the main function
    main(input_pdb_filename, output_folder)

    print(f"PDB file '{input_pdb_filename}' split into chains in the '{output_folder}' folder.")
