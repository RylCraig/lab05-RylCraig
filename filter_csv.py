# Part 2 (STRETCH) - filter the rows of a CSV file.
#
# This is a COMMAND-LINE program. You run it like:
#     python filter_csv.py people.csv city Oshawa
#
# The argument parser is finished for you. Complete the TODO.

import argparse
import csv


def main():
    parser = argparse.ArgumentParser(
        description="Print the rows of a CSV where a column has a given value.")
    parser.add_argument("filename", help="the CSV file to read")
    parser.add_argument("column", help="the name of the column to match on")
    parser.add_argument("value", help="the value to match")

    args = parser.parse_args()

    # TODO: open args.filename and read it with csv.reader. The first row is the
    #   header. Find the position of args.column within the header, then print every
    #   data row (its values joined by commas) whose value in that column equals
    #   args.value.

    with open(args.filename, 'r', newline='') as file:
        reader = csv.reader(file)

        # first row is header
        header = next(reader)
        col = header.index(args.column)

        # iterate over data
        for row in reader:
            # print(f'Current line: {row}')
            if row[col] == args.value:
                print(",".join(row))

    # with open(args.filename, 'r') as file:
    #     text = file.read()

    # rows = text.split('\n')
    # header = rows[0].split(',')
    # col = header.index(args.column)
    
    # # print(col)
    # # print(rows)

    # for row, line in enumerate(rows):

    #     if not line.strip():  # Skip blank lines
    #         continue

    #     tofind = line.split(',')    
    #     # print(f'{row}: {tofind}')
    #     if tofind[col] == args.value:
    #         # print(f'ans: {line}')
    #         print(f'{line}')

    # print(f'{header}')
    # print(f'{header.index(args.column)}')


if __name__ == "__main__":
    main()
