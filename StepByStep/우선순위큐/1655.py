import sys,heapq
N = int(sys.stdin.readline())
Mheap=[]
mheap=[]
result = []
for i in sys.stdin:
    if len(Mheap) == len(mheap):heapq.heappush(Mheap,-int(i))
    else: heapq.heappush(mheap,int(i))
    if mheap == []:
        result.append(int(i))
    else:
        A,B=heapq.heappop(Mheap),heapq.heappop(mheap)
        if -A > B:
            heapq.heappush(Mheap,-B)
            heapq.heappush(mheap,-A)
            A = -heapq.heappop(Mheap)
            result.append(A)
            heapq.heappush(Mheap,-A)
        else:
            result.append(-A)
            heapq.heappush(Mheap,A)
            heapq.heappush(mheap,B)
	
for i in result:
    print(i)
