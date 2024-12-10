"""
Solution:
- For each number, count how many times it occurs in the right list.
- Sum each score.
"""

def get_similarity_score(num, right_list):
    return num * right_list.count(num)

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    lines = input_file.readlines()

    left_list = []
    right_list = []

    for line in lines:
        numbers = line.strip('\n').split('   ')
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

    total_similarity_score = 0
    for num in left_list:
        total_similarity_score += get_similarity_score(num, right_list)
    print(total_similarity_score)