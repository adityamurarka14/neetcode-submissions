class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            res = stones[0] - stones[1]
            if res == 0:
                stones.pop(0)
                stones.pop(0)
            else:
                stones.pop(1)
                stones[0] = res
                stones.sort(reverse=True)
        return stones[0] if len(stones) == 1 else 0
