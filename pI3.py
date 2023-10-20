'''
Progran to find the ph of protein sequence
'''

from Bio.SeqUtils.ProtParam import ProteinAnalysis

def find_ph(protein_sequence):
# Create a ProteinAnalysis object
    protein_analyzer = ProteinAnalysis(protein_sequence)

# Calculate the isoelectric point (pI)
    pI = protein_analyzer.isoelectric_point()
    return pI
