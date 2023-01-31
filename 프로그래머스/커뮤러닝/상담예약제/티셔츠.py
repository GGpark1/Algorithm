def solution(people, tshirts):
    cnt = 0
    for p in people:
        if not tshirts:
            break
        if p in tshirts:
            tshirts.remove(p)
            cnt += 1
        else:
            p -= 1
            if p in tshirts:
                p += 1
                tshirts.remove(p)
                cnt += 1

    return cnt


people = [1, 2, 3]
tshirts = [1, 1]
print(solution(people, tshirts))
