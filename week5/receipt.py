"""
CSE 111 - Week 5

Author: Randy Jones

"""

import csv
from os import path

cur_dir = path.dirname(path.realpath(__file__))

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    result = {}

    with open(path.join(cur_dir, filename), 'rt') as csv_file:
        csv_rows = csv.reader(csv_file)
        next(csv_rows)
        for row in csv_rows:
            result[row[key_column_index]] = row

    return result


def main():
    products_dict = read_dictionary('products.csv', 0)
    print("All Products")
    print(products_dict)

    with open(path.join(cur_dir, 'request.csv'), 'rt') as request_file:
        csv_rows = csv.reader(request_file)
        next(csv_rows)
        print("Requested Items")
        for product_num, quantity in csv_rows:
            _, product_name, product_price = products_dict[product_num]
            print(f"{product_name}: {quantity} @ {product_price}")

if __name__ == '__main__':
    main()