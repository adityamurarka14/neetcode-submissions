class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        n = len(temperatures)
        output = [0] * n
        # for i in range(n):
        #     for j in range(i,n):
        #         if temperatures[j] > temperatures[i]:
        #             output[i] = j - i
        #             break
        # return output 
        
        # stack = []
        # for i,t in enumerate(temperatures):
        #     while stack and t > stack[-1][0]:
        #         stackT, stackInd = stack.pop()
        #         output[stackInd] = i - stackInd
        #     stack.append((t,i))

        # return output

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if output[j] == 0:
                    j = n
                    break
                j += output[j]
            
            if j < n:
                output[i] = j - i
        return output