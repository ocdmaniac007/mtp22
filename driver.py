# driver.py
'''
Driver Code for all other programs
'''
# from pdb2fasta import pdb_to_fasta
from isBasic_Acidic import classify_polarity
from hydropathy import calculate_gravy_score,classify_hydrophobicity
from pI import isoelectric_point
from aromatic import find_aromaticity
from instability import instability_index
from flexibility import flexibility
from mw import molecular_weight
from secondary_struct import secondary_structure_fraction
# from ramachandra import ramachandra_plot



seq='GHMELKREEITLLKELGSGQFGVVKLGKWKGQYDVAVKMIKEGSMSEDEFFQEAQTMMKLSHPKLVKFYGVCSKEYPIYIVTEYISNGCLLNYLRSHGKGLEPSQLLEMCYDVCEGMAFLESHQFIHRDLAARNCLVDRDLCVKVSDFGMTRYVLDDQYVSSVGTKFPVKWSAPEVFHYFKYSSKSDVWAFGILMWEVFSLGKMPYDLYTNSEVVLKVSQGHRLYRPHLASDTIYQIMYSCWHELPEKRPTFQQLLSSIEPLREKDKH'

def main():
    # Input

    # pdb_file=input("Enter the pdb file name:")
    # input_pdb_file = pdb_file+'.pdb'
    # output_fasta_file = pdb_file+"_fasta"
    # #Sequence Properties    
    # seq=pdb_to_fasta(input_pdb_file, output_fasta_file)


    polarity=classify_polarity(seq)
    print(f"The protein is classified as {polarity}.")
    gravy_score = calculate_gravy_score(seq)
    hydrophobicity = classify_hydrophobicity(gravy_score)
    print(f"The protein is classified as {hydrophobicity}.")
    ph=isoelectric_point(seq)
    print(f"The isoelectric point (pI) of the protein is: {ph:.2f}")
    aro=find_aromaticity(seq)
    print(f"The aromacity (aro) of the protein is: {aro:.2f}")
    index=instability_index(seq)
    print(f"The instability index (idx) of the protein is: {index:.2f}")
    flex=flexibility(seq)
    for aa, flex_value in zip(seq, flex):
        print(f"Amino Acid: {aa}, Flexibility: {flex_value:.2f}")
    mw=molecular_weight(seq)
    print(f"The molecular weight(mw) of the protein is: {mw:.2f}")
    ss=secondary_structure_fraction(seq)
    print(f"The fraction of helix: {ss[0]:.2f}")
    print(f"The fraction of turn: {ss[1]:.2f}")
    print(f"The fraction of sheet: {ss[2]:.2f}")
    #Structutral Properties
    # ramachandra_plot(pdb_file)







    

if __name__ == '__main__':
    main()
