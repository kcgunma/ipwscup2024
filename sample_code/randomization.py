import csv
import random
import sys

def random_replace(input_file, output_file, header_name, p):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames  # Get the header row
        
        if header_name not in fieldnames:
            raise ValueError(f"Header '{header_name}' not found in the CSV file.")
        
        # Collect all unique values from the specified header
        values = set()
        rows = []
        for row in reader:
            value = row[header_name]
            values.add(value)
            rows.append(row)
        
        if not values:
            raise ValueError(f"No values found in the header '{header_name}'.")

    # Perform replacement
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        
        for row in rows:
            if random.random() > p:  # With probability 1-p, replace the value
                row[header_name] = random.choice(list(values))
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py input_file output_file header_name p")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        header_name = sys.argv[3]
        p = float(sys.argv[4])
        
        if not (0 <= p <= 1):
            print("Error: Probability p must be between 0 and 1.")
        else:
            try:
                random_replace(input_file, output_file, header_name, p)
                print(f"CSV file with replaced values saved as '{output_file}'")
            except Exception as e:
                print(f"Error: {e}")
