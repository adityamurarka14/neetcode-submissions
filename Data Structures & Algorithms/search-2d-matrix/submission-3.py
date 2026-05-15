class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     print(matrix[i][0], matrix[i][len(matrix[i]) - 1])
        #     if not target >= matrix[i][0] and not target <= matrix[i][len(matrix[i]) - 1]:
        #         break
        #     else:
        #         for j in range(len(matrix[i])):
        #             if target == matrix[i][j]:
        #                 return True
        # return False
        # rowLen, colLen = len(matrix), len(matrix[0])
        # top, bot = 0, rowLen - 1
        # while top <= bot:
        #     mid = (top + bot) // 2
        #     if target > matrix[mid][-1]:
        #         top = mid + 1
        #     elif target < matrix[mid][0]:
        #         bot = mid - 1
        #     else:
        #         break
    
        # if not (top <= bot):
        #     return False
        # mid = (top + bot) //2
        # l , r = 0, colLen - 1
        # while l <=r:
        #     m = (l + r) // 2 
        #     if target > matrix[mid][m]:
        #         l = m + 1
        #     elif target < matrix[mid][m]:
        #         r = m - 1
        #     else:
        #         return True
        # return False

        row, col = len(matrix), len(matrix[0])

        l, r = 0, row * col - 1
        while l  <= r:
            m = (l + r) // 2
            cr, cc = m // col, m % col
            if target > matrix[cr][cc]:
                l = m + 1
            elif target < matrix[cr][cc]:
                r = m - 1
            else:
                return True
        return False