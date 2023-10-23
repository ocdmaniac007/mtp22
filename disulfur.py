# '''
# Note that disulfide bond length is about 2.05 A
# Source-Wikipedia (https://en.wikipedia.org/wiki/Disulfide)
# Sun MA, Wang Y, Zhang Q, Xia Y, Ge W, Guo D. Prediction of reversible disulfide based on features from local structural signatures. BMC Genomics. 2017 Apr 4;18(1):279. doi: 10.1186/s12864-017-3668-8. PMID: 28376774; PMCID: PMC5379614.
# '''



# from Bio.PDB import PDBParser, PPBuilder
# def disulphur(file):
#     parser = PDBParser()
#     structure = parser.get_structure("protein_name", file)
#     cys_residues = []
#     for model in structure:
#         for chain in model:
#             for residue in chain:
#                 if residue.get_resname() == "CYS":
#                     cys_residues.append(residue)
#     for i in range(len(cys_residues)):
#         for j in range(i+1, len(cys_residues)):
#             res1 = cys_residues[i]
#             res2 = cys_residues[j]
#             sg1 = res1["SG"]
#             sg2 = res2["SG"]
#             distance = sg1 - sg2
#             if distance<=2.05:
#                 print(f"Disulfide bond length between CYS{res1.id[1]} and CYS{res2.id[1]}: {distance}")

# disulphur('1ilg.pd')


from Bio.PDB import PDBParser, Selection
import numpy as np

def calc_disulphide_bond_length(filename):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('protein_name', filename)
    model = structure[0]

    # Get all cysteine residues
    cysteines = Selection.unfold_entities(structure, 'R')
    cysteines = [residue for residue in cysteines if residue.get_resname() == 'CYS']

    # Calculate distances between sulfur atoms 
    distances = []
    for residue_one in cysteines:
        for residue_two in cysteines:
            if residue_one != residue_two:
                try:
                    atom_one = residue_one['SG']
                    atom_two = residue_two['SG']
                    diff_vector = atom_one.coord - atom_two.coord
                    distance = np.sqrt(np.sum(diff_vector * diff_vector))
                    if distance <= 2.05:  # Only include distances <= 2.05 angstroms
                        distances.append((residue_one.id[1], residue_two.id[1], distance))
                except KeyError:
                    continue
    return distances

def disulfur(file):
    distances = calc_disulphide_bond_length(file)  # replace with your PDB file

    for res_one, res_two, distance in distances:
        print(f'Distance between CYS {res_one} and CYS {res_two} is {distance} angstroms')
