'''
Program to find molecular wt from fasta seq
'''
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def molecular_weight(protein_sequence):
# Create a ProteinAnalysis object
    protein_analyzer = ProteinAnalysis(protein_sequence)

# Calculate the molecular wt (mw)
    mw = protein_analyzer.molecular_weight()
    return mw
