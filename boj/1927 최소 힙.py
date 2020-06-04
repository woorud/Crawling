import heapq, sys
n = int(sys.stdin.readline())
minheap = []
heapq.heapify(minheap)

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(minheap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(minheap)[1])
        except:
            print(0)