class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] < target:       # target is bigger than everything here, try next row
                continue

            l, r = 0, len(row) - 1     # fresh bounds for each row
            while l <= r:
                mid = l + (r - l) // 2
                if row[mid] > target:
                    r = mid - 1
                elif row[mid] < target:
                    l = mid + 1        # move the LEFT bound
                else:
                    return True
            return False               # this was the only row that could hold it
        return False