# #!/usr/bin/env python3
"""
This script removes all 'baseline' blocks from any CSV files in the
'trial_orders' directory, since baseline blocks are irrelevant when testing
outside of a scanner.

You need to install the python package pandas if you don't already have it
prior to running this script.
"""
import os

import pandas as pd

def is_csv_file(fname):
    if not fname.endswith('.csv'):
        return False
    if fname.startswith('.') or fname.startswith('~'):
        return False
    return True

TRIAL_ORDERS_DIR_PATH = '../trial_orders'

def main():
    t_o_dir_files = os.listdir(TRIAL_ORDERS_DIR_PATH)

    csv_fpaths = []

    for f in t_o_dir_files:
        if is_csv_file(f):
            csv_fpaths.append(os.path.join(TRIAL_ORDERS_DIR_PATH, f))

    for fp in csv_fpaths:
        df = pd.read_csv(fp)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        baseline_mask = df.target_path.str.match('baseline')
        nobaseline_df = df[~baseline_mask]
        nobaseline_df.to_csv(fp)

if __name__ == '__main__':
    main()
