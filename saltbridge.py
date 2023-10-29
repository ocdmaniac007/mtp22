'''
https://en.wikipedia.org/wiki/Salt_bridge_(protein_and_supramolecular)
'''

import Bio.PDB
import numpy as np

# Define a function to calculate the distance between two atoms
def calculate_distance(atom1, atom2):
    coord1 = atom1.get_coord()
    coord2 = atom2.get_coord()
    return np.linalg.norm(coord1 - coord2)

# Define a function to find salt bridges
def find_salt_bridges(pdb_file_path, distance_cutoff=4.0):
    parser = Bio.PDB.PDBParser(QUIET=True)
    structure = parser.get_structure("protein", pdb_file_path)

    salt_bridges = []

    for model in structure:
        for chain in model:
            for residue1 in chain:
                if Bio.PDB.is_aa(residue1):
                    for atom1 in residue1:
                        if atom1.get_name() in ['NZ', 'NH1', 'NH2']:  # Check for positively charged atoms
                            for residue2 in chain:
                                if Bio.PDB.is_aa(residue2):
                                    for atom2 in residue2:
                                        if atom2.get_name() in ['OD1', 'OD2', 'OE1', 'OE2']:  # Check for negatively charged atoms
                                            distance = calculate_distance(atom1, atom2)
                                            if distance <= distance_cutoff:
                                                amino_acid1 = residue1.get_resname()
                                                amino_acid2 = residue2.get_resname()
                                                salt_bridges.append((amino_acid1, amino_acid2, distance))
    
    return salt_bridges

# Specify the input PDB file path
pdb_file_path = "3sxs.pdb"

# Call the function to find salt bridges
salt_bridges = find_salt_bridges(pdb_file_path)

# Print the salt bridges, their lengths, and the involved amino acids
for salt_bridge in salt_bridges:
    amino_acid1, amino_acid2, distance = salt_bridge
    print(f"Salt Bridge: {amino_acid1} - {amino_acid2}, Distance: {distance:.2f} Å")
