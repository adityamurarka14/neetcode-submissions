class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # nums.sort()
        # res = 0
        # streak = 0
        # curr = nums[0]
        # i = 0
        # while i < len(nums):
        #     if curr != nums[i]:
        #         curr = nums[i]
        #         streak = 0
        #     while i < len(nums) and nums[i] == curr:
        #         i+= 1
        #     streak += 1
        #     curr += 1
        #     res = max(res, streak)
        # return res

        numset = set(nums)
        longest = 0

        for num in numset:
            if (num - 1) not in numset:
                length = 1
                while(num + length) in numset:
                    length += 1
                longest = max(length, longest)
        return longest