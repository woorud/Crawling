def solution(scoville, K):
    import heapq

    h = []
    for i in scoville:
        heapq.heappush(h, i)

    answer = 0
    while h[0] < K:
        try:
            heapq.heappush(h, heapq.heappop(h) + 2 * heapq.heappop(h))
        except:
            return -1
        answer += 1


    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))