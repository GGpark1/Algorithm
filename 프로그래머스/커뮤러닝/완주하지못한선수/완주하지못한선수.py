def solution(participant, completion):
    res = ''
    same_name = ''
    p_dict = dict.fromkeys(participant, 0)
    c_dict = dict.fromkeys(completion, 0)

    for name in participant:
        p_dict[name] += 1

    for name in completion:
        c_dict[name] += 1

    for name in participant:
        if name not in c_dict:
            return name
        elif p_dict[name] != c_dict[name]:
            return name


p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]

print(solution(p, c))
