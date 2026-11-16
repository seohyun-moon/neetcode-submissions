class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Brute Force

        #array 1~9 to check
        nums = [0] * 9

        for i in range(0, 9):
            nums[i] = i + 1
        
        # check row
        for i in range(0, 9):
            row_check = nums
            seen = set()
            for j in range(0, 9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        # check column
        for i in range(0, 9):
            col_check = nums
            seen = set()
            for j in range(0,9):
                val = board[j][i]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        # check box
        for br in range(0, 3):
            for bc in range(0,3):
                seen = set()
                for i in range(br*3, br*3+3):
                    for j in range(bc*3, bc*3+3):
                        val = board[i][j]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        
        return True