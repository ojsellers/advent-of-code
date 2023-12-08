"""
Day two solve
"""


f = list(open('puzzle_in.txt', 'r'))
items = [(f_.replace('\n', '')) for f_ in f]


def get_valid(passwords):

    correct = 0

    for password in passwords:
        
        split_password = password.split(': ')
        pass_ = split_password[1]
        
        split_two = split_password[0].split('-')
        lower = split_two[0]

        split_three = split_two[1].split(' ')
        upper = split_three[0]
        letter = split_three[1]
        
        if int(lower) <= pass_.count(letter) <= int(upper):
            correct += 1

    return correct


def get_valid_rule2(passwords):

    correct = 0

    for password in passwords:
        
        split_password = password.split(': ')
        pass_ = split_password[1]
        
        split_two = split_password[0].split('-')
        lower = split_two[0]

        split_three = split_two[1].split(' ')
        upper = split_three[0]
        letter = split_three[1]
        
        if (pass_[int(lower)-1] == letter) is not (pass_[int(upper)-1] == letter):
            correct += 1

    return correct


print(get_valid(items))
print(get_valid_rule2(items))