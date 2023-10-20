'''
Program to find the % of secondary structures
'''
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def secondary_structure_fraction(protein_sequence):
# Create a ProteinAnalysis object
    protein_analyzer = ProteinAnalysis(protein_sequence)

# Calculate the secondary structure (ss)
    ss = protein_analyzer.secondary_structure_fraction()
    return ss


