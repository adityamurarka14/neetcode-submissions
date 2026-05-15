class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        # res = []
        # charMapping = {2:['a','b','c'], 3:['d','e','f'],4:['g','h','i'], 5:['j','k','l'],
        # 6: ['m','n','o'], 7:['p','q','r', 's'], 8:['t','u','v'], 9:['w','x','y','z']}
        
        # def dfs(i, cur):
        #     if i == len(digits):
        #         res.append(cur)
        #         return
            
        #     for c in charMapping[int(digits[i])]:
        #         dfs(i + 1, cur + c)

        # dfs(0, "")
        res = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            tmp = []
            for curStr in res:
                for c in digitToChar[digit]:
                    print(c, digit, digitToChar[digit], curStr, res, tmp)
                    tmp.append(curStr + c)
            res = tmp
        return res
