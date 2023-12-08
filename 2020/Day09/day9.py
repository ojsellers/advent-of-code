"""
Day 9 solve
"""


f = list(open('puzzle_in.txt', 'r'))
items = [(f_.replace('\n', '')) for f_ in f]


def get_first_wrong_number(numbers):

    for i in range(25, len(numbers)):

        num_list = [int(num) for num in numbers[i-25:i]]

        if not check_valid(int(numbers[i]), num_list):
            return numbers[i]

    return False
        
        
def check_valid(number, num_list):

    for num in num_list:

        for num_ in num_list:

            if num == num_:
                continue

            if num + num_ == number:
                return True

    return False


wrong_num = get_first_wrong_number(items)
print(wrong_num)


def get_contiguous_nums(numbers, wrong_num):

    for i in range(2, len(numbers)):

        for j in range(len(numbers) - i):
            
            cont_nums = [int(num) for num in numbers[j:i]]

            if sum(cont_nums) == int(wrong_num):
                return min(cont_nums) + max(cont_nums)

    return False

        
print(get_contiguous_nums(items, wrong_num))