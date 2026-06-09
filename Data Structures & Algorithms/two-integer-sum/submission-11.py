class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myset = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in myset:
                return [myset[compliment], i]
            myset[nums[i]] = i