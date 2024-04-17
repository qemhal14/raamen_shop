from tabulate import tabulate
import access as acc

def table():

    table_with_index = []

    for i, row in enumerate(acc.table_dish[1:], start=1):
        indexed_row = [i] + row
        table_with_index.append(indexed_row)

    print(tabulate(table_with_index, headers=acc.table_dish[0]))
