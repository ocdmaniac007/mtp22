#Guruprasad K, Reddy BV, Pandit MW. Correlation between stability of a protein and its dipeptide composition: a novel approach for predicting in vivo stability of a protein from its primary sequence. Protein Eng. 1990 Dec;4(2):155-61. doi: 10.1093/protein/4.2.155. PMID: 2075190.

'''
Program to find the stability of protein
'''

from Bio.SeqUtils.ProtParam import ProteinAnalysis

def instability_index(protein_sequence):
# Create a ProteinAnalysis object
    protein_analyzer = ProteinAnalysis(protein_sequence)

# Calculate the instability index (idx)
    index = protein_analyzer.instability_index()
    return index
