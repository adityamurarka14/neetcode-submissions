class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]
        # return -1
        
        
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)
        # return -1

        
        # seen = [0] * len(nums)
        # for num in nums:
        #     if seen[num - 1]:
        #         return num
        #     seen[num - 1] = 1
        # return -1


        # for num in nums:
        #     idx = abs(num) - 1
        #     if nums[idx] < 0:
        #         return abs(num)
        #     nums[idx] *= -1
        #     print(idx, num)
        #     print(nums)
        # return -1


        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow