# from itertools import accumulate


# def solution(bell):
#     """
#     Part1.
#     빨간방울 == 1, 초록방울 == -1로 변경하고,
#     방울들의 누적합 구하기
#     """

#     bell = list(map(lambda x: -1 if x == 2 else 1, bell))
#     added_bell = [0] * (len(bell) + 1)

#     for i in range(1, len(bell)+1):
#         added_bell[i] = sum(bell[:i])

#     """
#     Part2.
#     같은 누적합 중 거리가 가장 먼 값 구하기
#     """

#     start_dict = {}
#     end_dict = {}

#     for i, num in enumerate(added_bell[1:]):
#         if num not in start_dict:
#             start_dict[num] = i
#         end_dict[num] = i

#     return max(end_dict[i] - start_dict[i] for i in end_dict)


# bell = [1, 1, 1, 1, 1, 1]
# print(solution(bell))


def solution(bell):

    start_dict = {}
    end_dict = {}

    for i, num in enumerate(accumulate([0]+[-1 if b == 1 else 1 for b in bell])):
        if num not in start_dict:
            start_dict[num] = i
        else:
            end_dict[num] = i

    return max([end_dict[i] - start_dict[i] for i in end_dict])


bell = [1, 2, 1, 1, 1, 2, 2, 1]
print(solution(bell))
