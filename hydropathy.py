#Kyte J, Doolittle RF. A simple method for displaying the hydropathic character of a protein. J Mol Biol. 1982 May 5;157(1):105-32. doi: 10.1016/0022-2836(82)90515-0. PMID: 7108955.

'''
Program to find hydropathy of protein using gravy score
'''

# Calculate the GRAVY (Grand Average of Hydropathy) score for a protein sequence
def calculate_gravy_score(fasta_sequence):
    hydropathy_values = {
        'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
        'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
        'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
        'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
    }

    gravy_score = sum(hydropathy_values[aa] for aa in fasta_sequence)

    return gravy_score

def classify_hydrophobicity(gravy_score):
    if gravy_score > 0:
        return "Hydrophobic"
    elif gravy_score < 0:
        return "Hydrophilic"
    else:
        return "Neutral"

