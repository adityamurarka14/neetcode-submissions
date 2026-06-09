from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        print(groups)
        for str in strs:
            key = "".join(sorted(str))
            groups[key].append(str)
        return list(groups.values())