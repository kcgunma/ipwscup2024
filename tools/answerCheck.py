import argparse
import sys

import pandas as pd

def count_matching_cells(file1, file2):
    # read CSV file
    df1 = pd.read_csv(file1, header=None)
    df2 = pd.read_csv(file2, header=None)

    if df1.shape != df2.shape:
        print("Error: The CSV files do not have the same shape.")
        return

    matching_count = (df1.values == df2.values).sum()

    return matching_count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('Bx_csv_prefix', help='Prefix of the csv file to be used for the answer (e.g., B32x).')
    parser.add_argument('E_csv_prefix', help='Prefix of the csv file for the attack result (e.g., E32).')
    args = parser.parse_args()

    file1 = f'{args.Bx_csv_prefix}.csv'
    file2 = f'{args.E_csv_prefix}.csv'

    count = count_matching_cells(file1, file2)
    print(f"Number of matching cells: {count}")
