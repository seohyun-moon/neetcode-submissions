class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 1. sqaure each number
        squared = []

        for n in nums:
            squared.append(n * n)

        # 2. sort
        return sorted(squared)