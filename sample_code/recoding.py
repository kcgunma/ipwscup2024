import csv
import sys

def replace_values(input_file, output_file, header_name, cbv, cav):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames  # Get the header row
        
        if header_name not in fieldnames:
            raise ValueError(f"Header '{header_name}' not found in the CSV file.")
        
        # Prepare for output
        rows = []
        for row in reader:
            if row[header_name] == old_value:
                row[header_name] = new_value
            rows.append(row)
    
    # Write the modified rows to the output file
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        writer.writerows(rows)  # Write the modified rows

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python recoding.py input_file output_file header_name old_value new_value")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        header_name = sys.argv[3]
        old_value = sys.argv[4]
        new_value = sys.argv[5]
        
        try:
            replace_values(input_file, output_file, header_name, old_value, new_value)
            print(f"CSV file with values replaced saved as '{output_file}'")
        except Exception as e:
            print(f"Error: {e}")
