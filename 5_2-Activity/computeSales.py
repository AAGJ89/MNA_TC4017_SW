"""
Programming exercises 
Arturo Alfonso Gallardo Jasso
A01795510
computeSales.py Rev1.2
"""
# pylint: disable=invalid-name

# Libraries
import sys
import time
import json
from pathlib import Path

print("Program info: computeSales Rev1.0")

# Argument Vector with Try-Except to verify if the file provided is an argument
try:
    price_filename = sys.argv[1]
    sales_filename = sys.argv[2]
except IndexError:
    print("Error 1! Format to invoke the program is:\n"
          "python computeSales.py priceCatalogue.json TCX.salesRecord.json")
    sys.exit(1)

# Define paths
price_filename = Path(price_filename)
sales_directory = Path(sales_filename.split('.')[0])
sales_file_path = sales_directory / sales_filename

time_tracking = time.time()
item_list = []
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

# Conversion for price list to dictionary
price_data = {
    item["title"]: item["price"]
    for item in price_list
    if "title" in item and "price" in item
}

# Verify sales record file exists
try:
    with sales_file_path.open('r', encoding='utf-8') as file:
        sales_data = json.load(file)
except FileNotFoundError:
    print(f"Error 2! File not found: {sales_file_path}")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Error 3! Invalid JSON format in file: {sales_file_path}")
    sys.exit(1)

# Compute total cost

total_cost = 0
for sale in sales_data:
    try:
        product = sale["Product"]
        quantity = int(sale["Quantity"])
        if product in price_data:
            total_cost += price_data[product] * quantity
        else:
            print(f"Error 4! Product '{product}'not found in catalogue.")
            invalid_data.append(product)
    except (KeyError, ValueError):
        print(f"Error 5! Invalid data: {sale}")
        invalid_data.append(str(sale))

# Formatting results
results = f"Directory: {sales_directory}\nTotal Sales Cost: ${total_cost:.2f}"
results += f"\nTime elapsed: {time.time() - time_tracking:.4f} seconds\n"

print(results)

# Save results to file
with Path("SalesResults.txt").open("w", encoding='utf-8') as file:
    file.write(results)

print("Results saved in SalesResults.txt")
