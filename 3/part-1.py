"""
Solution:
- Parse?
- Has to look like mul -> parentheses -> number
- Strip whitespace
- But don't strip newlines?
"""

import re

def get_multiplications(sequence):
    multiplications = re.findall("mul\(\d+,\d+\)", sequence)
    return multiplications

def multiply_numbers(multiplication_string):
    stripped = multiplication_string.strip('mul(').strip(')').split(',')
    return int(stripped[0]) * int(stripped[1])

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    lines = input_file.readlines()
    lines = [line.strip('\n') for line in lines]
    
    sum_of_multiply = 0
    
    for line in lines:
        multiplications = get_multiplications(line)
        for m in multiplications:
            sum_of_multiply += multiply_numbers(m)

    print(sum_of_multiply)