class Solution:
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
                else:
                    num = int(board[i][j])
                    bit = 1 << (num - 1)
                    rows[i] |= bit
                    cols[j] |= bit
                    box_idx = (i // 3) * 3 + (j // 3)
                    boxes[box_idx] |= bit
        
        def get_possibilities(i, j):
            box_idx = (i // 3) * 3 + (j // 3)
            used = rows[i] | cols[j] | boxes[box_idx]
            return ~used & 0x1FF
        
        def find_best_cell():
            best_idx = -1
            best_possibilities = None
            best_count = 10
            
            for idx, (i, j) in enumerate(empty_cells):
                if board[i][j] == '.':
                    poss = get_possibilities(i, j)
                    count = bin(poss).count('1')
                    if count < best_count:
                        best_count = count
                        best_idx = idx
                        best_possibilities = poss
                        if count == 1:
                            break
            
            return best_idx, best_possibilities
        
        def backtrack():
            idx, poss = find_best_cell()
            if idx == -1:
                return True
            
            i, j = empty_cells[idx]
            box_idx = (i // 3) * 3 + (j // 3)
            
            while poss:
                bit = poss & -poss
                num = bit.bit_length()
                
                board[i][j] = str(num)
                rows[i] |= bit
                cols[j] |= bit
                boxes[box_idx] |= bit
                
                if backtrack():
                    return True
                
                board[i][j] = '.'
                rows[i] &= ~bit
                cols[j] &= ~bit
                boxes[box_idx] &= ~bit
                
                poss -= bit
            
            return False
        
        backtrack()





       