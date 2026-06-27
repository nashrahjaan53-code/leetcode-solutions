class Solution:
    def totalNQueens(self, n):
        cols = [False] * n
        pos_diag = [False] * (2 * n)
        neg_diag = [False] * (2 * n)

        def backtrack(row):
            if row == n:
                return 1
            count = 0
            for c in range(n):
                if cols[c] or pos_diag[row + c] or neg_diag[row - c + n]:
                    continue

                cols[c] = True
                pos_diag[row + c] = True
                neg_diag[row - c + n] = True

                count += backtrack(row + 1)
                cols[c] = False
                pos_diag[row + c] = False
                neg_diag[row - c + n] = False

            return count

        return backtrack(0)
         

        
   

       
        