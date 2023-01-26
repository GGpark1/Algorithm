from functools import cmp_to_key


def compare(x, y):
    if x+y < y+x:
        return 1
    else:
        return -1


def solution(number):
    number = list(map(str, number))
    number = sorted(number, key=cmp_to_key(compare))
    return ''.join(number)


number = [3, 30, 34, 5, 9]
print(solution(number))
