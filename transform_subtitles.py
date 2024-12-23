
import os
import re

# Input and output folder paths
input_folder = ''  # Folder with your input files
output_folder = ''  # Folder where you want to save the processed files

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to remove unwanted content
def remove_pre_timestamp_content(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Regular expression pattern to match timestamp lines (e.g., 0.566s)
    timestamp_pattern = r'\d+\.\d+s'

    # Prepare a list to store the processed lines
    processed_lines = []

    # Iterate over the lines to remove unwanted timestamps
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if re.match(timestamp_pattern, line):  # If line is a timestamp
            if i + 1 < len(lines) and lines[i + 1].strip():  # Check if next line is not empty
                processed_lines.append(line + '\n')
                processed_lines.append(lines[i + 1])
                i += 2  # Skip the next line since it's already added
            else:
                i += 1  # Just move to the next line if next one is empty
        else:
            processed_lines.append(line + '\n')
            i += 1

    # Write the remaining lines to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(processed_lines)

# Process all .txt files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        # Apply the function to each file
        remove_pre_timestamp_content(input_file_path, output_file_path)

print("Processing completed.")
