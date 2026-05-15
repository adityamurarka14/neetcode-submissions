class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones.sort(reverse=True)
        # while len(stones) > 1:
        #     res = stones[0] - stones[1]
        #     if res == 0:
        #         stones.pop(0)
        #         stones.pop(0)
        #     else:
        #         stones.pop(1)
        #         stones[0] = res
        #         stones.sort(reverse=True)
        # return stones[0] if len(stones) == 1 else 0

        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            curr = heapq.heappop(max_heap)*-1 - heapq.heappop(max_heap)*-1

            if curr:
                heapq.heappush(max_heap, curr*-1)
        
        return heapq.heappop(max_heap)*-1 if len(max_heap) == 1 else 0
