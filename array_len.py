MOD = 10**9 + 7

class Solution:
    def zigZagArrays(self, n, l, r):
        m = r - l + 1
        size = 2 * m
        
        mat = [[0] * size for _ in range(size)]
        
        for prev in range(m):
            for v in range(prev + 1, m):
                mat[v][m + prev] = (mat[v][m + prev] + 1) % MOD
        
        for prev in range(m):
            for v in range(prev):
                mat[m + v][prev] = (mat[m + v][prev] + 1) % MOD
        
        def mat_mult(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                for k in range(n):
                    if A[i][k]:
                        for j in range(n):
                            C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C
        
        def mat_pow(mat, power):
            n = len(mat)
            res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            while power > 0:
                if power & 1:
                    res = mat_mult(res, mat)
                mat = mat_mult(mat, mat)
                power >>= 1
            return res
        
        state = [0] * size
        for i in range(m):
            for j in range(m):
                if i < j:
                    state[j] = (state[j] + 1) % MOD
                elif i > j:
                    state[m + j] = (state[m + j] + 1) % MOD
        
        if n == 2:
            return sum(state) % MOD
        
        mat = mat_pow(mat, n - 2)
        
        result = [0] * size
        for i in range(size):
            for j in range(size):
                result[i] = (result[i] + mat[i][j] * state[j]) % MOD
        
        return sum(result) % MOD