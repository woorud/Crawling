import heapq, sys
n = int(sys.stdin.readline())
absheap = []
heapq.heapify(absheap)

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(absheap, num)
    else:
        try:
