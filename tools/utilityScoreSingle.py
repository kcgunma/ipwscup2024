from concurrent.futures import ProcessPoolExecutor, as_completed
import argparse

import pandas as pd
import numpy as np

def load_data(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    return df1, df2

def find_max_mae_and_columns(file1, file2, parallel=1):
    df1, df2 = load_data(file1, file2)
    columns = list(set(df1.columns) & set(df2.columns))

    # Define pairs of column names to exclude.
    excluded_columns = {'Name', 'Gender', 'Age', 'Occupation', 'ZIP-code'}

    # Generate pairs of column names and filter out excluded pairs.
    column_pairs = set()
    for col1 in columns:
        for col2 in columns:
            if col1 != col2 and not (col1 in excluded_columns and col2 in excluded_columns):
                pair = tuple(sorted((col1, col2)))
                column_pairs.add(pair)

    err_dic = {}
    for pair in column_pairs:
      c1,c2 = pair
      column_pair = [c1, c2]
      freq1 = df1.value_counts(column_pair)
      freq2 = df2.value_counts(column_pair)
      err_dic[",".join(column_pair)] = (freq1 - freq2).abs().sum()

    # Normalization of MAE.
    max_mae_columns, max_mae = max(err_dic.items(), key=lambda x: x[1])
    normalize = 20000
    max_mae = max_mae / normalize

    return max_mae_columns, max_mae


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('org_csv', help='Distribution data after splitting (e.g., B32_3.csv)')
    parser.add_argument('ano_csv', help='Anonymized data (e.g., C32_3.csv)')
    parser.add_argument('--parallel', default=1, help='Number of parallel processing threads.')
    args = parser.parse_args()

    file1 = args.org_csv
    file2 = args.ano_csv
    parallel = args.parallel

    max_mae_columns, max_mae = find_max_mae_and_columns(file1, file2, parallel)
    us = "{:.3f}".format((1-max_mae)*100)
    max_mae_value = "{:.5f}".format(max_mae)
    print(f"Max Mean Absolute Error: {max_mae_value}")
    print(f"Columns with max MAE: {max_mae_columns}")
    print(f"Utility Score: {us}")
