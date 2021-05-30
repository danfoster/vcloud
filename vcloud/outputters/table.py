from pprint import pprint
from tabulate import tabulate

def table(input):
    print(tabulate(input, headers="keys"))
