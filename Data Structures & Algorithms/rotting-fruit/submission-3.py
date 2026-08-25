class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque() # to store all rotten banana
        good_banana = 0 # every minute check the length of it
        # visit = [[False]*COLS for _ in range(ROWS) ]

        def addCell(r,c):
            nonlocal good_banana
            # for a singel cell, if good banana, gets rotten,
            # if empty, just return
            if r < 0 or r>=ROWS or c < 0 or c >= COLS or grid[r][c] == 0 :
                return 
            if grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r,c))
                good_banana -= 1
                # visit[r][c] == False
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    good_banana += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        minutes = 0
        if good_banana == 0:
                return minutes
        while q:
            if good_banana == 0:
                return minutes
            for _ in range(len(q)):
                r,c = q.popleft()
                addCell(r-1,c)
                addCell(r+1,c)
                addCell(r, c-1)
                addCell(r, c+1)
            minutes += 1
        return -1

            
        
        