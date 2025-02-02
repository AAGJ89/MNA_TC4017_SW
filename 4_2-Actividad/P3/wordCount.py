"""
Problem 3. Count Words
Arturo Alfonso Gallardo Jasso
A01795510
wordCount.py Rev1.1
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

# Handling data in the file
for line in all_lines:
    try:
        word = line.strip()
        item_list.append(word)
    except ValueError:
        invalid_data.append(line.strip())

if not item_list:
    print("Error 3! No data in the file")
    sys.exit(1)

if invalid_data:
    print(f"Error 4! Invalid data: {', '.join(invalid_data)}")

# Count word frequency
word_counter = {}
for word in item_list:
    if word in word_counter:
        word_counter[word] +=1
    else:
        word_counter[word]= 1

# Nested rearrangement of the words frequencies (higher first)
word_counter_list = list(word_counter.items())
n = len(word_counter_list)
for i in range(n):
    for j in range(0, n-i-1):
        if word_counter_list[j][1]<word_counter_list[j+1][1]:
            word_counter_list[j],word_counter_list[j+1]=word_counter_list[j+1],word_counter_list[j]

# Calculating length of the columns
max_word_width = max(len(word) for word, count in word_counter_list)
max_freq_width = max(len(str(count)) for word, count in word_counter_list)

# Display results
print("\nWord Count:")
header = f"{'Row Labels':<{max_word_width}}{'Count':<{max_freq_width}}"
print(header)

results = header + "\n"
for word, count in word_counter_list:
    line = (
        f"{word:<{max_word_width}}"
        f"{count:<{max_freq_width}}"
    )
    print(line)
    results += line + "\n"


#Time
elapsed_time = time.time() - time_tracking

elapsed_time_string = f"Time elapsed on execution of this program: {elapsed_time:.4f} seconds"
results += elapsed_time_string
print (elapsed_time_string)
with open("WordCountResults.txt", "w", encoding='utf-8') as file:
    file.write(results)

print("\nThese results are stored in WordCountResults.txt under P3 folder")
