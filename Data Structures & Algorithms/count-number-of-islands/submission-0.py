class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for i in range(rows)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        res = 0
        
        def checkIsland(r,c):
            if visited[r][c] == True:
                return 
            visited[r][c] = True
            if grid[r][c] == "1":
                for (i,j) in directions:
                    new_row = r+i
                    new_col = c+j
                    if new_row >=0 and new_row <rows and new_col >= 0 and new_col < cols:
                        if grid[new_row][new_col] == "1":
                            checkIsland(new_row, new_col)
                        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited[r][c] == False:
                    print(r,c)
                    res += 1
                    checkIsland(r,c)
        return res

        