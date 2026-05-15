class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                myStack.append(s[i])
            else:
                if myStack:
                    poppedEle = myStack.pop()
                    if poppedEle == "{" and s[i] == "}":
                        continue
                    elif poppedEle == "(" and s[i] == ")":
                        continue
                    elif poppedEle == "[" and s[i] == "]":
                        continue
                    else:
                        return False
                else:
                    return False
        if myStack == []: 
            return True 
        else: 
            return False 