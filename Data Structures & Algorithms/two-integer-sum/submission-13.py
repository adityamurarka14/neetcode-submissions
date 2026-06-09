class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # myset = {}

        # for i in range(len(nums)):
        #     compliment = target - nums[i]
        #     if compliment in myset:
        #         return [myset[compliment], i]
        #     myset[nums[i]] = i

        nums = [(num,i) for i, num in enumerate(nums)]
        nums.sort()
        print(nums)
        i, j = 0 , len(nums) - 1

        while i < j:
            sum = nums[i][0] + nums[j][0]
            print(nums[i][0], nums[j][0], sum)
            if target == sum:
                return sorted([nums[i][1], nums[j][1]])
            elif sum > target:
                j -= 1
            else:
                i += 1
        return []