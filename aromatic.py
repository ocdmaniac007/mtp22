#Lobry JR, Gautier C. Hydrophobicity, expressivity and aromaticity are the major trends of amino-acid usage in 999 Escherichia coli chromosome-encoded genes. Nucleic Acids Res. 1994 Aug 11;22(15):3174-80. doi: 10.1093/nar/22.15.3174. PMID: 8065933; PMCID: PMC310293.
'''
Program to find the aromatcity of protein sequence
'''

from Bio.SeqUtils.ProtParam import ProteinAnalysis

def find_aromaticity(protein_sequence):
# Create a ProteinAnalysis object
    protein_analyzer = ProteinAnalysis(protein_sequence)

# Calculate the aromaticity (aro)
    aro = protein_analyzer.aromaticity()
    return aro