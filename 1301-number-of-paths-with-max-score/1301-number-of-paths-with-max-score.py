class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        


        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        

        dp[n-1][n-1] = [0, 1]
        
     
        dirs = [(1, 0), (0, 1), (1, 1)]
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X':
                    continue
                if i == n-1 and j == n-1:
                    continue
                    
                max_score = -1
                ways = 0
                
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if ni < n and nj < n and board[ni][nj] != 'X' and dp[ni][nj][1] > 0:
                        score = dp[ni][nj][0]
                        if score > max_score:
                            max_score = score
                            ways = dp[ni][nj][1]
                        elif score == max_score:
                            ways = (ways + dp[ni][nj][1]) % MOD
                
                if max_score != -1:
                    val = 0
                    if board[i][j] != 'E':
                        val = int(board[i][j])
                    dp[i][j] = [max_score + val, ways]
        
        return [dp[0][0][0], dp[0][0][1] % MOD] if dp[0][0][1] > 0 else [0, 0]





        