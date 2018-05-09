import pandas as pd
import sys


def compute_expense(filename):

    fn = pd.read_csv(filename)
    df = fn[['Category', 'Cost']]
    gb = df.groupby(df['Category'])
    sum_by_cat = gb.sum()
    total_cost = sum_by_cat.sum()

    return sums, total_cost


if __name__ == '__main__':
    finalename = sys.argv[1]
    sums, total_cost = compute_expense(finalename)
    print "expenses by category:\n", sums
    print "total cost = ", total_cost