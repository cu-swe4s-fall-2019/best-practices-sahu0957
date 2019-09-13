import sys
import math
import argparse

parser = argparse.ArgumentParser(
    description="calculate mean and std. dev of a column in an input file")

parser.add_argument("file_name", help="input file", type=str)

parser.add_argument("column_number",
                    help="column index of input file",
                    type=int)
args = parser.parse_args()


def col_mean_stdev_finder():
    # Assign user inputs to variables
    file_name = args.file_name
    col_num = args.column_number

    # Open input file
    try:
        f = open(file_name, 'r')
        V = []
    except (FileNotFoundError):
        sys.stderr.write("The specified file doesn't exist! Exiting...\n")
        exit()
    # Create a list from the input file,
    # using input column number
    try:
        for l in f:
            A = [int(x) for x in l.split()]
            V.append(A[col_num])
    except (IndexError):
        sys.stderr.write("Column index not found! Exiting...\n")
        exit()
    # Calculate mean of the column
    mean = sum(V)/len(V)

    # Calculate standard deviation
    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    # Print determined outputs
    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    col_mean_stdev_finder()
