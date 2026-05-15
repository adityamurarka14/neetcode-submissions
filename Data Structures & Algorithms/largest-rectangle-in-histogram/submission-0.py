class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        myStack = []
        for index, height in enumerate(heights):
            start = index
            while myStack and myStack[-1][1] > height:
                stackIndex, stackHeight = myStack.pop()
                maxArea = max(maxArea, stackHeight * (index - stackIndex))
                start = stackIndex
            myStack.append((start, height))
        
        for index, height in myStack:
            maxArea = max(maxArea, height * (len(heights) - index))
        return maxArea