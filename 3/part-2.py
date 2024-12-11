"""
Solution:
- Toggle do is ON.
- Find a don't(), toggle do OFF.
- Find a do(), toggle do ON.
- Get do and don't from sequences, in masterlist including all muls.
"""

import re

def get_instructions(sequence):
    multiplications = re.findall("mul\(\d+,\d+\)|don\'t\(\)|do\(\)", sequence)
    return multiplications

def multiply_numbers(multiplication_string):
    stripped = multiplication_string.strip('mul(').strip(')').split(',')
    return int(stripped[0]) * int(stripped[1])

def follow_instructions(instructions):
    do_multiply = True
    sum_of_instructions = 0
    for i in range(0, len(instructions)):
        instruction = instructions[i]
        if instruction == "do()":
            do_multiply = True
        elif instruction == "don't()":
            do_multiply = False
        elif do_multiply:
            sum_of_instructions += multiply_numbers(instruction)
        else:
            continue
    return sum_of_instructions

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    text = input_file.read().strip('\n')
    
    instructions = get_instructions(text)
    sum_of_multiply = follow_instructions(instructions)
    
    print(sum_of_multiply)