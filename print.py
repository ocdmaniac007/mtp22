import os

# Path to the folder containing tm-align result files
folder_path = "/home/mt0/22CS60R49/MTP/tm_align_results"

# Minimum tm-align score threshold
threshold = 0.7

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".tmalign"):  # Assuming your tm-align result files have the ".tmalign" extension
        with open(os.path.join(folder_path, filename), "r") as file:
            lines = file.readlines()

            # Parse the tm-align results
            query_seq = None
            for line in lines:
                if line.startswith("Query seq"):
                    query_seq = line.strip()
                elif query_seq and line.startswith("TM-score"):
                    tm_score = float(line.split(":")[1])
                    if tm_score >= threshold:
                        print(query_seq)
                        print(f"{filename}|tm-score|{line.strip()}")

# Make sure to replace "path/to/tm-align/results" with the actual path to your folder.
