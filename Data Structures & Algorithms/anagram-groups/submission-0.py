class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedString = ''.join(sorted(s))
            res[sortedString].append(s)
        return list(res.values())