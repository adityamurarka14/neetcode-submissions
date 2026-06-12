class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n2 complexity. 2 loops
        # result = [0] * len(nums)
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
            
        #     result[i] = prod
        
        # return result

        # 2 runs of O(n). Division method

        # prod, zero_count = 1, 0

        # for num in nums:
        #     if not num:
        #         zero_count += 1
        #     else:
        #         prod *= num
        
        # if zero_count > 1:
        #     return [0] * len(nums)
        
        # res = [0] * len(nums)
        # for i, num in enumerate(nums):
        #     if zero_count:
        #         res[i] = 0 if num else prod
        #     else:
        #         res[i] = prod//num
        
        # return res

        #Prefix and suffix arrys

        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n-1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]

        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res