import csv
import random
import sys

def swap_column_values(rows, header_names, n):
    for _ in range(n):
        # Randomly choose two different rows to swap values
        row1, row2 = random.sample(rows, 2)
        
        for header in header_names:
            if header in header_to_index:
                idx = header_to_index[header]
                # Swap values for the specified header
                row1[idx], row2[idx] = row2[idx], row1[idx]

def process_csv(input_file, output_file, header_names, n):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        headers = next(reader)  # Get the header row
        rows = list(reader)     # Convert remaining rows to a list
    
    global header_to_index
    header_to_index = {header: idx for idx, header in enumerate(headers) if header in header_names}
    
    # Swap column values
    swap_column_values(rows, header_names, n)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)  # Write the header row
        writer.writerows(rows)    # Write the modified rows

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py input_file output_file header1 [header2 ... headerN] n")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        header_names = sys.argv[3:-1]  # Get all header names
        n = int(sys.argv[-1])  # Get the number of swaps
        
        if not header_names:
            print("At least one header name must be specified.")
        else:
            process_csv(input_file, output_file, header_names, n)
            print(f"CSV file with swapped columns saved as '{output_file}'")
