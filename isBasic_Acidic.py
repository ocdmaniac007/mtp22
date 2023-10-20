# amino_acid_polarity.py
'''
Program to check if the given fasta seq acidic,basic or neutral
Please note Acidic(-1) Basic(+1) Neutral(0)
'''
def classify_polarity(fasta_sequence):
    # Define lists of amino acids considered acidic and basic
    acidic_aa = ['D', 'E']
    basic_aa = ['K', 'R', 'H']

    # Initialize counters for acidic, basic, and neutral amino acids
    acidic_count = 0
    basic_count = 0
    neutral_count = 0

    # Convert the sequence to uppercase for consistency
    fasta_sequence = fasta_sequence.upper()

    # Iterate through the sequence and count amino acids
    for aa in fasta_sequence:
        if aa in acidic_aa:
            acidic_count += 1
        elif aa in basic_aa:
            basic_count += 1
        else:
            neutral_count += 1

    # Determine the classification based on counts
    if acidic_count > basic_count:
        return -1
    elif basic_count > acidic_count:
        return 1
    else:
        return 0

