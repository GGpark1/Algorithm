def solution(number, k):
    num_list = list(number)
    num_list.append('0')
    count = 0
    i = 0
    while count <= k:
        if num_list[i] >= num_list[i+1]:
            i += 1
            continue
        else:
            for j in range(len(num_list[:i])+1):
                if num_list[j] < num_list[i+1] and num_list != '':
                    num_list[j] = ''
                    count += 1
                    if count >= k:
                        return ''.join(num_list)
            i += 1
    res = ''.join(num_list)

    return res


n = "1924"
k = 2
print(solution(n, k))
