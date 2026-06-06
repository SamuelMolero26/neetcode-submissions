class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #hashset approach for row + column (9x9)
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        #hashset to check for the 3x3 grid duplicates
        squares = collections.defaultdict(set)
        #key is (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if ((board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in squares[(r // 3), (c // 3)])):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3),(c // 3)].add(board[r][c])

        return True
