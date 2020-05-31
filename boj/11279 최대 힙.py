import heapq
import sys
n = int(sys.stdin.readline())
mh = []
heapq.heapify(mh)
for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(mh, -num)
    else:
        try:
            print(-1 * heapq.heappop(mh))
        except:
            print(0)