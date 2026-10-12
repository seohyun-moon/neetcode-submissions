class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        whole = []

        for m in matrix:
            for i in m:
                whole.append(i)

        if target in whole:
            return True
        return False