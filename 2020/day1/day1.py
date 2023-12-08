"""
Day one solve
"""


f = list(open('puzzle_in.txt', 'r'))
items = [(f_.replace('\n', '')) for f_ in f]
items.sort()
items = [int(item) for item in items]

def get_sum(nums):

    for num in nums:
        for num_ in nums:
        
            if num + num_ == 2020:
                return num * num_

print(get_sum(items))


def get_sum_3_nums(nums):

    for num in nums:
        for num_ in nums:
            for num__ in nums:
        
                if num + num_ + num__ == 2020:
                    return num * num_ * num__

print(get_sum_3_nums(items))