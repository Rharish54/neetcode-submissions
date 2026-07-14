class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colsHashmap = collections.defaultdict(set)
        rowsHashmap = collections.defaultdict(set)
        subBoxHashmap = collections.defaultdict(set)

        # we know dimensions: 9x9
        for row in range(9):
            for col in range(9):
                #first check if no value is present
                if board[row][col] == ".":
                    continue
                if(board[row][col] in rowsHashmap[row] or
                   board[row][col] in colsHashmap[col] or
                   board[row][col] in subBoxHashmap[(row // 3, col // 3)]): #int division
                   return False
                rowsHashmap[row].add(board[row][col])
                colsHashmap[col].add(board[row][col])
                subBoxHashmap[(row // 3, col // 3)].add(board[row][col])
        return True

