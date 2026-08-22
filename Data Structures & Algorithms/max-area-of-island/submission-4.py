class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for i in range(rows)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        res = 0
        temparea = 0
        
        def checkIsland(r,c):
            nonlocal temparea
            if visited[r][c] == True:
                return 
            temparea += 1
            visited[r][c] = True
            # if it is the island, checking surrounding area
            if grid[r][c] == 1:
                for (i,j) in directions:
                    new_row = r+i
                    new_col = c+j
                    if new_row >=0 and new_row <rows and new_col >= 0 and new_col < cols:
                        if grid[new_row][new_col] == 1 and visited[new_row][new_col] is False:
                            checkIsland(new_row, new_col)
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == False:
                    temparea = 0
                    checkIsland(r,c)
                    res = max(res, temparea)
        return res
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for i in range(rows)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        res = 0
        temparea = 0
        
        def checkIsland(r,c):
            nonlocal temparea
            if visited[r][c] == True:
                return 
            temparea += 1
            visited[r][c] = True
            # if it is the island, checking surrounding area
            if grid[r][c] == 1:
                for (i,j) in directions:
                    new_row = r+i
                    new_col = c+j
                    if new_row >=0 and new_row <rows and new_col >= 0 and new_col < cols:
                        if grid[new_row][new_col] == 1 and visited[new_row][new_col] is False:
                            checkIsland(new_row, new_col)
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == False:
                    temparea = 0
                    checkIsland(r,c)
                    res = max(res, temparea)
        return res
        