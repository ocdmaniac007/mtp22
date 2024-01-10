#onic residue pairs(R,K,H) : (D,E) falling within a distance of 6Å contribute to ionic interactions
#Ref: Tina, K. G., Bhadra R, and Srinivasan N.(2007) PIC: protein interactions calculator. Nucleic
#Acids Research 35, 473-476

from Bio import PDB
def ionicfun(atom1, atom2, resid1, resid2, dist=6):
    """
    Check for ionic interactions
    atom1, atom2: biopython class atom
    resid1, resid2: biopython class residues
    dist = distance(float) cutoff in Angstrom
    return: distance(float)  if < dist
    """
    if (
        (
            "N" in atom1.get_name()
            and len(atom1.get_name()) > 1
            and resid1.get_resname() in ["LYS", "ARG", "HIS"]
        )
        and (
            "O" in atom2.get_name()
            and len(atom2.get_name()) > 1
            and resid2.get_resname() in ["ASP", "GLU"]
        )
    ) or (
        (
            "O" in atom1.get_name()
            and len(atom1.get_name()) > 1
            and resid1.get_resname() in ["ASP", "GLU"]
        )
        and (
            "N" in atom2.get_name()
            and len(atom2.get_name()) > 1
            and resid2.get_resname() in ["LYS", "ARG", "HIS"]
        )
    ):
        d = atom1 - atom2
        if d < dist:
            return d
    return None

def find_ionic_interactions(pdb_file, distance_cutoff=6.0):
    """
    Find ionic interactions in a protein structure.
    
    Parameters:
    - pdb_file: str, path to the PDB file
    - distance_cutoff: float, distance cutoff for considering interactions (default: 6.0 Å)
    
    Returns:
    - List of dictionaries with information about ionic interactions
    """
    # Create a PDB parser
    parser = PDB.PDBParser(QUIET=True)

    # Load the PDB file
    structure = parser.get_structure('protein', pdb_file)

    # List to store ionic interactions
    ionic_interactions = []

    # Iterate through the structure
    for model in structure:
        for chain in model:
            for residue1 in chain:
                for atom1 in residue1:
                    for residue2 in chain:
                        for atom2 in residue2:
                            # Check for ionic interactions using the provided function
                            distance = ionicfun(atom1, atom2, residue1, residue2)
                            if distance is not None and distance < distance_cutoff:
                                ionic_interactions.append({
                                    'Residue1': f"{residue1.get_resname()} {atom1.get_id()}",
                                    'Residue2': f"{residue2.get_resname()} {atom2.get_id()}",
                                    'Distance': distance
                                })

    return ionic_interactions


pdb_file_path = '2acy.pdb'
ionic_interactions = find_ionic_interactions(pdb_file_path)

# Print the results
for interaction in ionic_interactions:
    print(f"Ionic Interaction between {interaction['Residue1']} and {interaction['Residue2']}: {interaction['Distance']:.3f} Å")
