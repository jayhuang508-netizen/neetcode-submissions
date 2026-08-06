class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # already non-decreasing, first check the last column, then check row
        potential_row = -1
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target <= matrix[i][n-1]:
                potential_row = i
                break
        if potential_row == -1:
            return False
        # then in the single row do the search
        row = matrix[potential_row][:]
        i = 0
        j = n -1
        while i<=j:
            m = i+(j-i)//2
            if row[m] < target:
                i = m+1
            elif row[m] > target:
                j = m-1
            else:
                return True
        return False

        
