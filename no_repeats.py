
""" pas terminer """

from itertools import permutations


def char_has_twin(index, string):
    if index >= len(string) - 1:
        return False
    else:
        return string[index] == string[index + 1]

def str_has_twins(string: str):
    return any(char_has_twin(index, string) for index in range(len(string)))

def perm_alone(string) :
    perms_twins = (str_has_twins(perm) for perm in permutations(string))
    perms_alone = filter(lambda perm: not perm, perms_twins)
    return len(list(perms_alone))


result1 = 'nnnbb'
print(perm_alone(result1))