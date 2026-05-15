class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        # for i in range(len(s)):
        #     if s[i] == "(" or s[i] == "{" or s[i] == "[":
        #         myStack.append(s[i])
        #     else:
        #         if myStack:
        #             poppedEle = myStack.pop()
        #             if poppedEle == "{" and s[i] == "}":
        #                 continue
        #             elif poppedEle == "(" and s[i] == ")":
        #                 continue
        #             elif poppedEle == "[" and s[i] == "]":
        #                 continue
        #             else:
        #                 return False
        #         else:
        #             return False
        # if myStack == []: 
        #     return True 
        # else: 
        #     return False
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in closeToOpen:
                if myStack and myStack[-1] == closeToOpen[i]:
                    myStack.pop()
                else:
                    return False
            else:
                myStack.append(i)
        
        return True if myStack == [] else False