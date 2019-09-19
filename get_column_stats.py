import sys
import math
import argparse


def parse_args():
    # Read input arguments, if the function is called as the main
    parser = argparse.ArgumentParser(
        description="calculate mean and std. dev of a column in an input file")

    parser.add_argument("data_file", help="input file", type=str)

    parser.add_argument("column_index",
                        help="column index of input file",
                        type=int)
    args = parser.parse_args()
    return args


def col_mean_finder(file_name, col_num):
    # Open input file
    try:
        f = open(file_name, 'r')
        V = []
    except FileNotFoundError as ex:
        sys.stderr.write('The specified file does not exist! Exiting...\n')
        raise ex
        sys.exit(1)
    # Create a list from the input file,
    # using input column number
    try:
        for l in f:
            A = [int(x) for x in l.split()]
            V.append(A[col_num])
    except (IndexError):
        sys.stderr.write("Column index not found! Exiting...\n")
        raise IndexError
        sys.exit(1)
    # Calculate mean of the column
    try:
        mean = sum(V)/len(V)
    except (ZeroDivisionError) as ex:
        sys.stderr.write("List is empty! Can't divide by 0. Exiting...\n")
        raise ZeroDivisionError
        sys.exit(1)
    except (ValueError):
        sys.stderr.write("List contains non-number entries! Exiting...\n")
        raise ValueError
        sys.exit(1)
    # Return determined outputs
    return('mean: ' + str(mean))


def col_stdev_finder(file_name, col_num):
    # Open input file
    try:
        f = open(file_name, 'r')
        V = []
    except (FileNotFoundError):
        sys.stderr.write("The specified file doesn't exist! Exiting...\n")
        raise FileNotFoundError
        sys.exit(1)
    # Create a list from the input file,
    # using input column number
    try:
        for l in f:
            A = [int(x) for x in l.split()]
            V.append(A[col_num])
    except (IndexError):
        sys.stderr.write("Column index not found! Exiting...\n")
        raise IndexError
        sys.exit(1)
    # Calculate mean, handling errors
    try:
        mean = sum(V)/len(V)
    except (ZeroDivisionError):
        sys.stderr.write("List is empty! Can't divide by 0. Exiting...\n")
        raise ZeroDivisionError
        sys.exit(1)
    except (ValueError):
        sys.stderr.write("List contains non-number entries! Exiting...\n")
        raise ValueError
        sys.exit(1)
    # Calculate standard deviation, handling exceptions
    try:
        stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / (len(V) - 1))
    except (ZeroDivisionError):
        sys.stderr.write("List contains less than 2 entries! Exiting...\n")
        raise ZeroDivisionError
        sys.exit(1)
    # Return determined outputs
    return('stdev:' + ' ' + str(stdev))


def main():
    # Run as main if this function is called directly
    args = parse_args()
    col_mean_finder(args.data_file, args.column_index)
    col_stdev_finder(args.data_file, args.column_index)


if __name__ == '__main__':
    main()
