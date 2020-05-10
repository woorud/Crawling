def solution(board, moves):
    pick = []
    cnt = 0
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                got = j[i-1]
                j[i-1] = 0
                if len(pick) == 0:
                    pick.append(got)
                elif len(pick) > 0 and pick[-1] != got:
                    pick.append(got)
                else:
                    cnt += 2
                    pick.pop()
                break
    return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))