"""
Problem 2. Converter
Arturo Alfonso Gallardo Jasso
A01795510
computeSales.py Rev1.0
"""
# pylint: disable=invalid-name

# Libraries
import sys
import time
import json
from pathlib import Path

# Using Argument Vector with Try-Except to verify if the file provided is an argument
try:
    price_filename = sys.argv[1]
    sales_filename = sys.argv[2]
except IndexError:
    print("Error 1! Format to invoke the program is: python computeSales.py priceCatalogue.json salesRecord.json")
    sys.exit(1)

# Define paths
price_filename = Path(price_filename)  # Price catalogue is in the main directory
sales_directories = ["TC1", "TC2", "TC3"]

time_tracking = time.time()
#item_list = []
invalid_data = []

# Using Try-Except to find the file
try:
    with price_filename.open('r', encoding='utf-8') as file:
        price_list = json.load(file)
except FileNotFoundError:
    print(f"Error 2! File not found: {price_filename}")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Error 3! Invalid JSON format in file: {price_filename}")
    sys.exit(1)