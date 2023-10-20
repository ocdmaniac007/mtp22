# pdb_to_fasta_biopython.py

from Bio import SeqIO

def pdb_to_fasta(input_pdb_file, output_fasta_file):
    """
    Convert a PDB file to FASTA format using Biopython.

    :param input_pdb_file: Input PDB file path.
    :param output_fasta_file: Output FASTA file path.
    """
    sequences = []
    for record in SeqIO.parse(input_pdb_file, "pdb-seqres"):
        sequences.append(record.seq)
    #print(type(sequences))
    seq = ''.join(str(item) for item in sequences)

    return seq

if __name__ == '__main__':
    # Example usage when running this script directly
    input_pdb_file = 'input.pdb'
    output_fasta_file = 'output.fasta'
    pdb_to_fasta(input_pdb_file, output_fasta_file)
