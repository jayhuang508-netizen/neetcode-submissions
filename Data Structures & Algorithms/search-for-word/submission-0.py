class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        def dfs(r,c,i):
            if i == len(word):
                # find
                return True
            if (r < 0 or c < 0 or r>=rows or c>= cols) or (word[i] != board[r][c] or board[r][c] == "#"):
                return False
            res = False
            # check the position of (r,c)
            board[r][c] = "#"
            for (m,n) in directions:
                res = res or dfs(r+m, c+n,i+1)
            board[r][c] = word[i]
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

                

        