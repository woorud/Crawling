def solution(name):
    name = list(name)
    default = ['A']*len(name)
    cnt = 0
    idx = 0
    while True:
        right = 1
        left = 1
        if name[idx] != 'A':
            if ord(name[idx])-ord('A')>13:
                cnt += 26-(ord(name[idx])- ord('A'))
            else:
                cnt += ord(name[idx])-ord('A')
            name[idx] = 'A'

        if name == default:
            break
        else:
            for i in range(1, len(name)):
                if name[idx+i] == 'A':
                    right += 1
                else:
                    break
                if name[idx-i] == 'A':
                    left += 1
                else:
                    break

            if right > left:
                cnt += left
                idx -= left
            else:
                cnt += right
                idx += right
    return cnt

print(solution('JEROEN'))
print(solution('JAN'))