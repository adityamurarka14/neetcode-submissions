class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums == []:
            return []

        res = []
        l = 0
        for i in range(k, len(nums) + 1):
            res.append(max(nums[l:i]))
            l += 1
        return res