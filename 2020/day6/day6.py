"""
Day 6 solve
"""


f = list(open('puzzle_in.txt', 'r'))
items = [(f_.replace('\n', '')) for f_ in f]

last_i = 0
groups = []


for i, item in enumerate(items):
    if item == '':
        groups.append(' '.join(items[last_i: i]))
        last_i = i + 1


groups.append(' '.join(items[last_i:]))


def get_questions_answered(groups):

    return [set(group.replace(' ', '')) for group in groups]


def get_questions_all_answered(groups, qs_answered):

    qs_all_answered = 0

    for q_answer, group in zip(qs_answered, groups):

        people = group.split()

        for q in q_answer:

            if all([q in p for p in people]):
                qs_all_answered += 1

    return qs_all_answered




qs_answered = get_questions_answered(groups)

print(sum([len(q) for q in qs_answered]))

print(get_questions_all_answered(groups, qs_answered))