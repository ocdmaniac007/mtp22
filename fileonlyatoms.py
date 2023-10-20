def filter_pdb_file(pdb_file):
    # Create an output file in the output folder with the same name
    output_file = "3sxs_A_new.pdb"
    
    with open(pdb_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Check if the line starts with "ATOM"
            if line.startswith('ATOM'):
                outfile.write(line)

filter_pdb_file('3sxs_A.pdb')

