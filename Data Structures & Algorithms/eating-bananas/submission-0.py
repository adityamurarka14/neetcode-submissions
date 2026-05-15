class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l , r = 1, max(piles)
        minK = r
        while l <= r:
            mid = (l + r) // 2
            currentHours = 0
            for banana in piles:
                currentHours += math.ceil(banana / mid)
            
            if currentHours <= h:
                r = mid - 1
                minK = min(mid, minK)
            else:
                l = mid + 1
        return minK