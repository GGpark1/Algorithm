def solution(booked, unbooked):
    _booked = []
    _unbooked = []
    result = []

    for t, n in booked:
        h, m = t.split(':')
        h = int(h) * 60
        m = int(m)
        t = h+m
        _booked.append([t, n])

    for t, n in unbooked:
        h, m = t.split(':')
        h = int(h) * 60
        m = int(m)
        t = h+m
        _unbooked.append([t, n])

    end_time = 0
    while _booked:
        if len(result) == 0:
            if _booked[0][0] <= _unbooked[0][0]:
                result.append(_booked[0][1])
                end_time = _booked[0][0] + 10
                _booked.pop(0)
            else:
                result.append(_unbooked[0][1])
                end_time = _unbooked[0][0] + 10
                _unbooked.pop(0)

        if not _booked:
            break

        if _unbooked:
            if _booked[0][0] <= end_time:
                result.append(_booked[0][1])
                end_time = _booked[0][0] + 10
                _booked.pop(0)
            elif _booked[0][0] > end_time:
                if _booked[0][0] > _unbooked[0][0]:
                    result.append(_unbooked[0][1])
                    end_time = _unbooked[0][0] + 10
                    _unbooked.pop(0)
                else:
                    result.append(_booked[0][1])
                    end_time = _booked[0][0] + 10
                    _booked.pop(0)
        else:
            result.append(_booked[0][1])
            _booked.pop(0)

    if _unbooked:
        for _, n in _unbooked:
            result.append(n)

    return result


booked = [["00:2", "hae"]]
unbooked = [["00:10", "hee"], ["00:35", "joo"]]
print(solution(booked, unbooked))
