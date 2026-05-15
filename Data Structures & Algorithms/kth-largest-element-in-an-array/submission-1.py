class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for i in nums:
            heapq.heappush(maxHeap, -i)
        
        heapq.heapify(maxHeap)

        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        
        return -maxHeap[0]


