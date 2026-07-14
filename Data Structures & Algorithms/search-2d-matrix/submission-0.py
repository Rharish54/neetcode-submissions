class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #got the algo right

        rows, cols = len(matrix), len(matrix[0])

        bottom, top = rows - 1, 0

        while top <= bottom:
            r = int((top + bottom) / 2)
            #last value in row r (greatest value in row r)
            if target > matrix[r][-1]:
                top = r + 1
            #first value in row r (lowest value in row r)
            elif target < matrix[r][0]:
                bottom = r - 1
            else:
                break #break exits out of loops, continue goes to next iteration of the loop

        if not (top <= bottom): #this means target is outside bounds of matrix
            return False
        
        #r = (top + bottom) // 2
        i, j = 0, cols - 1

        while i <= j:
            m = (i + j) // 2
            if target > matrix[r][m]:
                i = m+1
            elif target < matrix[r][m]:
                j = m - 1
            else:
                return True
        
        return False
        


