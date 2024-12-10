from itertools import pairwise

"""
Solution:
- Check if increasing or decreasing (use sorted function?)
- Check the maximum distance between two numbers
"""

def is_monotonic(report):
    is_increasing = all(i < j for i, j in zip(report, report[1:]))
    is_decreasing = all(i > j for i, j in zip(report, report[1:]))
    return is_increasing or is_decreasing

def has_good_diff(report):
    max_diff = abs(max(b-a for (a,b) in pairwise(report)))
    min_diff = abs(min(b-a for (a,b) in pairwise(report)))
    return max([max_diff, min_diff]) <= 3 and min([max_diff, min_diff]) >= 1

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    lines = input_file.readlines()
    lines = [line.strip('\n') for line in lines]
    
    safe_reports = 0
    
    for line in lines:
        report = [int(item) for item in line.split(' ')]
        if is_monotonic(report) and has_good_diff(report):
            safe_reports += 1

    print(safe_reports)