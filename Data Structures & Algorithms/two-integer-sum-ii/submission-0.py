class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mydict = defaultdict(int)

        for i in range(len(numbers)):
            remainder = target - numbers[i]
            if mydict[remainder]:
                return [mydict[remainder], i+ 1]
            mydict[numbers[i]] = i + 1
        return []