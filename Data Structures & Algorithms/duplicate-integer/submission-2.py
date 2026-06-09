class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = []
        for num in nums:
            if num in myset:
                return True
            myset.append(num)
        
        return False