"""
Problem 2. Converter
Arturo Alfonso Gallardo Jasso
A01795510
convertNumbers.py Rev1.0
"""
# pylint: disable=invalid-name

# Libraries
import sys
import time

# Using Argument Vector with Try-Except to verify if the file provided is an argument
try:
    filename = sys.argv[1]

except IndexError:
    print("Error 1! Format to invoke the program is: python computeStatistics.py TCX.txt")
    sys.exit(1)

time_tracking = time.time()
item_list = []
invalid_data = []

# Using Try-Except to find the file
try:
    with open(filename, 'r', encoding='utf-8') as file:
        all_lines = file.readlines()
except FileNotFoundError:
    print(f"Error 2! File not found: {filename}")
    sys.exit(1)

# Handling invalid data in the file
for line in all_lines:
    try:
        num = int(line.strip())
        item_list.append(num)
    except ValueError:
        invalid_data.append(line.strip())

if not item_list:
    print("Error 3! No data in the file")
    sys.exit(1)

if invalid_data:
    print(f"Error 4! Invalid data: {', '.join(invalid_data)}")

# Integer to binary
binary=[]
for number in item_list:
    n = int(number)
    binary_conversion = bin(abs(n))[2:]
    if number < 0:
        binary_conversion = '-' + binary_conversion
    binary.append(binary_conversion)

# Integer to hexadecimal
hexadecimal=[]
for number in item_list:
    hexadecimal_conversion = hex(abs(number))[2:].upper()
    if number < 0:
        hexadecimal_conversion = '-' + hexadecimal_conversion    
    hexadecimal.append(hexadecimal_conversion)

# Calculating length of the columns
max_num_width = max(len(str(num)) for num in item_list) + 2
max_bin_width = max(len(bin) for bin in binary) + 2
max_hex_width = max(len(hex) for hex in hexadecimal) + 2

#Conversion
print("\nConversion Results:")
header = f"{'NUMBER':<{max_num_width +3}}{'BIN':<{max_bin_width +3 }}{'HEX':<{max_hex_width + 3}}"
print(header)

for num, binary_conversion, hexadecimal_conversion in zip(item_list, binary, hexadecimal):
    print(f"{num:<{max_num_width}}   {binary_conversion:<{max_bin_width}}   {hexadecimal_conversion:<{max_hex_width}}")

elapsed_time = time.time() - time_tracking

results = header +"\n"
for num, binary_conversion, hexadecimal_conversion in zip(item_list, binary, hexadecimal):
    line = f"{num:<{max_num_width + 3}}{binary_conversion:<{max_bin_width + 3}}{hexadecimal_conversion:<{max_hex_width + 3}}"
    print(line)
    results += line +"\n"

elapsed_time_string = f"Time elapsed on execution of this program: {elapsed_time:.4f} seconds"
results += elapsed_time_string

with open("ConvertionResults.txt", "w", encoding='utf-8') as file:
    file.write(results)
    
print("\nThese results are stored in ConvertionResults.txt under P2 folder")

#Time
print(elapsed_time_string)

