
from Bio.PDB import PDBParser, Selection
import numpy as np

def hydrophobic_interaction(file):
    # hydrophobic=['A','V','L','I','M','F','W','P','Y']
    # parser=PDB.PDBParser()
    # io=PDB.PDBIO()
    # struct=parser.get_structure("pdb",file)
    # for model in struct:
    #     for chain in model:
    #         for residue in chain:
    #             for atom in residue:
    #                 x,y,z=atom.get_vector()
    #                 print(x,y,z)



    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('protein_name', file)
    model = structure[0]
    hydrophobic=['ALA','VAL','LEU','ILE','MET','PHE','TRP','PRO','TYR']

    # Get all  residues
    aa = Selection.unfold_entities(structure, 'R')
    aa_ = [residue for residue in aa if residue.get_resname() in hydrophobic ]

hydrophobic_interaction("2acy_new.pdb")