# Define the input and output file paths
input_file_path = 'Defects.txt'
output_file_path = 'defects.txt'

# Open the input file for reading
with open(input_file_path, 'r') as input_file:
    # Read the content of the file
    file_content = input_file.read()

# Replace newline characters with spaces
file_content = file_content.replace('\n', ' ')

# Open the output file for writing
with open(output_file_path, 'w') as output_file:
    # Write the modified content back to the file
    output_file.write(file_content)
