"""
Solution:
- Sort both ascending.
- Measure distance.
- Add each.
"""

def get_distance(left_num, right_num):
    return abs(left_num - right_num)

def get_total_distance(left_list = [], right_list = []):
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)

    total_distance = 0
    for i in range(0, len(sorted_left_list)):
        total_distance += get_distance(sorted_left_list[i], sorted_right_list[i])
    
    return total_distance

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    lines = input_file.readlines()

    left_list = []
    right_list = []

    # print(lines)
    for line in lines:
        numbers = line.strip('\n').split('   ')
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

    # print(left_list)
    # print(right_list)
    print(get_total_distance(left_list, right_list))