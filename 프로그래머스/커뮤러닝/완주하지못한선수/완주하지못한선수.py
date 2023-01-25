
# def solution(participant, completion):
#     """1차 풀이"""
#     res = ''
#     same_name = ''
#     p_dict = dict.fromkeys(participant, 0)
#     c_dict = dict.fromkeys(completion, 0)

#     for name in participant:
#         p_dict[name] += 1

#     for name in completion:
#         c_dict[name] += 1

#     for name in participant:
#         if name not in c_dict:
#             return name
#         elif p_dict[name] != c_dict[name]:
#             return name


# p = ["mislav", "stanko", "mislav", "ana"]
# c = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    """2차 풀이"""
    p_dict = {}
    for name in participant:
        p_dict[name] = p_dict.get(name, 0) + 1

    for name in completion:
        p_dict[name] -= 1

    non_complete = [key for key, value in p_dict.items() if value != 0]
    answer = non_complete[0]
    return answer


p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]

print(solution(p, c))
