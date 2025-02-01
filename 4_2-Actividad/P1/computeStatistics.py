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
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error 2! File not found: {filename}")
    sys.exit(1)

# Handling invalid data in the file
for line in lines:
    try:
        num = float(line.strip())
        item_list.append(num)
    except ValueError:
        # print(f"Error 3! Invalid data: {line.strip()}")
        invalid_data.append(line.strip())

if not item_list:
    print("Error 3! No data in the file")
    sys.exit(1)

if invalid_data:
    print(f"Error 4! Invalid data: {', '.join(invalid_data)}")

# Computation. Descriptive statistics: Mean, Median, Mode, Standard Deviation, and Variance
item_qty = len(item_list)

# Mean
mean = sum(item_list) / item_qty

# Median
item_list.sort()
mid_number = item_qty // 2
if item_qty % 2 == 0:
    median = (item_list[mid_number - 1] + item_list[mid_number]) / 2
else:
    median = item_list[mid_number]

# Mode
frequency = {}
for number in item_list:
    frequency[number] = frequency.get(number, 0) + 1
max_freq = max(frequency.values())
mode = [key for key, value in frequency.items() if value == max_freq]

mode = max(mode) 

# Standard deviation
variance = sum((x - mean) ** 2 for x in item_list) / len(item_list)

# Variance
std_dev = variance ** 0.5

# Results management (Printing into screen, saving into file)
results = (
    f"Mean: {mean:.2f}\n"
    f"Median: {median:.2f}\n"
    f"Mode: {mode}\n"
    f"Variance: {variance:.2f}\n"
    f"Standard Deviation: {std_dev:.2f}"
)

print(results)
with open("StatisticsResults.txt", "w", encoding='utf-8') as file:
    file.write(results)

print("\nResults are stored in StatisticsResults.txt")

# Time
elapsed_time = time.time() - time_tracking
print(f"Time elapsed on execution: {elapsed_time:.4f} seconds")