class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = set()
        for num in nums:
            if num in myDict:
                return True
            myDict.add(num)
        return False