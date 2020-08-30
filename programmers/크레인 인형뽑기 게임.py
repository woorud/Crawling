def solution(board, moves):
    crash = []
    res = []
    for move in moves:
        for m in range(len(board)):
            if board[m][move-1] != 0:
                crash.append(board[m][move-1])
                board[m][move-1] = 0

                if len(crash) > 1:
                    if crash[-1] == crash[-2]:
                        res.append(crash[-2])
                        crash.pop(-1)
                        crash.pop(-1)
                break
    return len(res) * 2


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))