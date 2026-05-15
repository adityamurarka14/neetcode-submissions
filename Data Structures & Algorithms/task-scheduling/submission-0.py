class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count =  Counter(tasks)
        # maxHeap = [-cnt for cnt in count.values()]

        # heapq.heapify(maxHeap)
        # time = 0
        # myQ = deque()

        # while maxHeap or myQ:
        #     time += 1

        #     if maxHeap:
        #         cnt = 1 + heapq.heappop(maxHeap)
        #         if cnt:
        #             myQ.append([cnt, time + n])
            
        #     if myQ and myQ[0][1] == time:
        #         heapq.heappush(maxHeap, myQ.popleft()[0])
        
        # return time

        freq = Counter(tasks)
        maxf = max(freq.values())
        maxCount = sum(1 for v in freq.values() if v == maxf)

        return max(len(tasks), (maxf - 1) * (n + 1) + maxCount)