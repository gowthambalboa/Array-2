#tc: O(m*n)
#sc: O(1)

class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def countAlive(board,i,j):
            directions = [[-1,0],[1,0],[0,1],[0,-1],[-1,1],[1,-1],[1,1],[-1,-1]]
            res = 0
            for d in directions:
                new_row = i + d[0]
                new_col = j + d[1]
                if new_row >=0 and new_row<m and new_col >= 0 and new_col < n and (board[new_row][new_col] == 1 or board[new_row][new_col] == 2):
                    res += 1
            return res
        
        
        for i in range(m):
            for j in range(n):
                alive = countAlive(board,i,j)
                if board[i][j] == 1 and (alive < 2 or alive > 3): # Under and over population
                    board[i][j] = 2  # 2 means 1 -> 0 (dying)
                if board[i][j] == 0 and alive == 3: # Reproduction
                    board[i][j] = 3 # 3 means 0 -> 1 (comes alive)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 0
                if board[i][j] == 3: board[i][j] = 1
                    
        return board

obj = Solution()
print(obj.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))