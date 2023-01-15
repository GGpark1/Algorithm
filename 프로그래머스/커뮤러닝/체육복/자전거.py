def solution(cost, order):

    # part 1
    order.sort()
    _order = [order[0]]
    for i, (m, n) in enumerate(sorted(order)[1:]):
        _order.append([m - order[i][0], n])

    # part 2
    stack = []
    for m, n in _order:
        while stack:
            _m, _n = stack[-1]
            if _m / _n < m / n:
                break
            stack.pop()
            m, n = m + _m, n + _n
        stack.append([m, n])

    # part 3
    """
    m : 작업 개월 수
    n : 총 작업량
    t : 월별 작업량
    p : 누진세
    """
    answer = 0  # 처음 금액은 0원
    for m, n in stack:  # 특정 기간동안(m) 작업해야하는 양(n)을 for문에 넣음
        p_prev = 0
        for t, p in cost:  # 전기사용량(자전거 생산량)(t)과 누진세(p)를 for문에 넣음
            # 월별 작업량 * 개월 수가 전체 작업량보다 적으면(->남는 작업량이 있다는 뜻->문제에서 정한 범위를 넘었다는 뜻->현재 누진범위를 적용해야 한다는 뜻) for문을 마저 순회
            # 월별 작업량 * 개월 수가 전체 작업량보다 많으면(->그 기간에 정해진 작업량이 끝났다는 뜻) => 그 다음 작업으로 이동
            if m * t >= n:
                break
            answer += (n - m * t) * (p - p_prev)  # 넘긴 갯수 * 차액
            p_prev = p

    return answer


cost = [[0, 10], [50, 20], [100, 30], [200, 40]]
order = [[3, 50], [7, 200], [8, 200]]

print(solution(cost, order))
