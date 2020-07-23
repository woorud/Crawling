def dfs(_cur, _cnt):
    global ans
    global _num
    if not _cnt:
        ans = max(ans, int(''.join(_num)))
        return
    for i in range(_cur, len(_num)):
        for j in range(i + 1, len(_num)):
            if _num[j] >= _num[i]:
                _num[j], _num[i] = _num[i], _num[j]
                dfs(i, _cnt - 1)
                _num[j], _num[i] = _num[i], _num[j]


def _change(_cnt):
    global ans
    if not _cnt:
        ans = int(''.join(_num))
        return
    _num[-1], _num[-2] = _num[-2], _num[-1]
    _change(_cnt - 1)


T = int(input())
for i in range(1, T + 1):
    _num, _cnt = input().split()
    _num = list(_num)
    ans = 0
    dfs(0, int(_cnt))
    if not ans:
        _change(int(_cnt))
    print('#{}'.format(i), ans)