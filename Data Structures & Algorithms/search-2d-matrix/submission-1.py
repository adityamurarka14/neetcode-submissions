class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            print(matrix[i][0], matrix[i][len(matrix[i]) - 1])
            if not target >= matrix[i][0] and not target <= matrix[i][len(matrix[i]) - 1]:
                break
            else:
                for j in range(len(matrix[i])):
                    if target == matrix[i][j]:
                        return True
        return False