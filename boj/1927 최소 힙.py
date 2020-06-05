import heapq, sys
n = int(sys.stdin.readline())
minheap = []
heapq.heapify(minheap)

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(minheap, num)
    else:
        try:
            print(heapq.heappop(minheap))
        except:
            print(0)