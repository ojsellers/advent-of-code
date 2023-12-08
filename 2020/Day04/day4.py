"""
Test.py
"""


import re
import numpy as np


def get_correct_passports(passports, fields):
    """
    Get passports with correct fields from list of passports
    """
    correct_passports = []

    for passport in passports:

        correct_fields = 0
       
        for field in fields:

            if field in passport:
                correct_fields += 1
        
        if correct_fields == len(fields):
            correct_passports.append(passport)

    return correct_passports    


def get_valid_passports(passports, fields):
    """
    Get passports with valid entries for a list of passports with the correct
    fields
    """
    valid_passports = []

    for passport in passports:

        split_passport = passport.split(' ')

        if check_valid_field(split_passport):
            valid_passports.append(passport)

    return valid_passports


def check_valid_field(split_passport):

    for field in split_passport:

            split_field = field.split(':')

            if not check_valid(split_field[0], split_field[1]):
                return False

    return True


def check_valid(field, contents):

    if field == 'pid':
        if len(contents) == 9 and contents.isdigit():
            return True
        return False

    elif field == 'byr':
        if 1920 <= int(contents) <= 2002:
            return True
        return False
    
    elif field == 'iyr':
        if 2010 <= int(contents) <= 2020:
            return True
        return False

    elif field == 'eyr':
        if 2020 <= int(contents) <= 2030:
            return True
        return False

    elif field == 'hgt':
        if contents[-2:] == 'cm':
            if 150 <= int(contents[:-2]) <= 193:
                return True
            return False

        elif contents[-2:] == 'in':
            if 59 <= int(contents[:-2]) <= 76:
                return True
            return False
        return False

    elif field == 'hcl':
        if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', contents):
            return True
        return False

    elif field == 'ecl':
        if contents in 'amb blu brn gry grn hzl oth.':
            return True
        return False

    elif field == 'cid':
        return True

    return False


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


f = list(open('puzzle_in.txt', 'r'))
items = [(f_.replace('\n', '')) for f_ in f]

last_i = 0
passports = []


for i, item in enumerate(items):
    if item == '':
        passports.append(' '.join(items[last_i: i]))
        last_i = i + 1


passports.append(' '.join(items[last_i:]))


fields = [
    'byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:',
]

correct_fields = get_correct_passports(passports, fields)

valid_passports = get_valid_passports(correct_fields, fields)

print(len(valid_passports))