#Vihinen M, Torkkila E, Riikonen P. Accuracy of protein flexibility predictions. Proteins. 1994 Jun;19(2):141-9. doi: 10.1002/prot.340190207. PMID: 8090708.
'''
Program to find the flexibility of each amino acid in fasta seq
'''
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def flexibility(protein_sequence):
# Create a ProteinAnalysis object
    protein_analyzer = ProteinAnalysis(protein_sequence)

# Calculate the flexibility (flex)
    flex = protein_analyzer.flexibility()
    return flex
