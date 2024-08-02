import sys
import argparse
import re

from utilityScoreSingle import find_max_mae_and_columns

def validate_id(id_value):
    """ Check that the ID is a two-digit number. """
    if not re.match(r'^\d{2}$', id_value):
        raise argparse.ArgumentTypeError("Invalid ID '{}'. ID must be a two-digit number.".format(id_value))
    return id_value

def us(id, input_path, output_path, parallel):
    """ Function to calculate a usefulness score. """
    min_us = 100.0
    for i in range(10):
        file1 = f"{input_path}/B{id}_{i}.csv"
        file2 = f"{output_path}/C{id}_{i}.csv"
        max_mae_columns, max_mae = find_max_mae_and_columns(file1, file2, parallel)
        us = "{:.3f}".format((1 - max_mae) * 100)
        max_mae_value = "{:.5f}".format(max_mae)
        print(f"Max Mean Absolute Error ({i}): {max_mae_value}")
        print(f"Columns with max MAE ({i}): {max_mae_columns}")
        print(f"Utility Score ({i}): {us}")
        if float(us) < float(min_us):
            min_us = us
    print(f"Utility Score: {min_us}")
    return min_us

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--id', type=validate_id, help='Please specify ID with two digits.')
    parser.add_argument('--input', default=".", help='Specify the path of the folder where the distribution data (e.g. B00_0.csv) is located.')
    parser.add_argument('--output', default=".", help='Specify the path of the folder where the anonymised data (e.g. C00_0.csv) is located.')
    parser.add_argument('--parallel', type=int, default=1, help='Specify parameters for parallel execution.')
    args = parser.parse_args()

    if args.id:
        id = args.id
    else:
        try:
            with open('id.txt', 'r') as file:
                id = file.read().strip()
            validate_id(id)  # Validate the ID from file
        except Exception as e:
            sys.exit(f"Error reading ID: {e}")

    min_us = us(id, args.input, args.output, args.parallel)
    print(min_us)

