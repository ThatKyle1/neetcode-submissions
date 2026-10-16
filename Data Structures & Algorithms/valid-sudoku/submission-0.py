class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validSquare(startRow, startCol):
            checkSet = set()
            temp = startCol
            for i in range(0,3):
                startCol = temp
                for j in range(0,3):
                    index = board[startRow][startCol]
                    if index == '.':
                        startCol += 1
                        continue
                    if index not in checkSet:
                        checkSet.add(index)
                    else:
                        return False
                    startCol += 1
                startRow += 1
            return True

        # max row = 9 max col = 9 
        # 0,2 3, 5  6, 8 
        valid = ['1','2','3','4','5','6','7','8','9']

        # check every row if duplicate return false O(N)
        
        for row in board:
            checke = set()
            for bla in row:
                if bla == '.':
                    continue
                if bla not in checke:
                    checke.add(bla)
                else:
                    return False
        


        # nexted loop of 9 x 9 , each time checking [c][r + 1] (O(N^2))
        
        for row in range(0,9):
            check = set()
            for col in range(0,9):
                index = board[col][row]
                if index == '.':
                    continue
                if index not in valid:
                    return False # false if not a valid 1-9 
                if index not in check:
                    check.add(index)
                else:
                    return False



        # max row = 9 max col = 9 
        # 0,2 3, 5  6, 8 
        
        #0,0    0, 3 , 0, 6 

        # 3 ,0 3, 3, 3, 6

        # 6,0   6, 3   6, 6

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                if not validSquare(i, j):
                    return False
        
        return True






                
            