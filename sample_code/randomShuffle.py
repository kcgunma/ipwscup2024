import csv
import random
import sys

def shuffle_csv(input_file, output_file):
    # Open the input CSV file for reading
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        headers = next(reader)  # Get the header row
        rows = list(reader)     # Convert remaining rows to a list
    
    # Shuffle the order of rows
    random.shuffle(rows)
    
    # Open the output CSV file for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)  # Write the header row
        writer.writerows(rows)    # Write the shuffled rows

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python shuffle_csv.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        shuffle_csv(input_file, output_file)
        print(f"Shuffled CSV file saved as '{output_file}'")
