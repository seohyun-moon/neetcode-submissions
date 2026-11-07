class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # fixed sized window of k
        l, minW = 0, float("inf")

        # count the number of W, min and keep the smallest one
        # if l+k is out of bound, return min
        while l < (len(blocks) - k + 1):
            count = 0
            for r in range(l, l + k):
                if blocks[r] == "W":
                    count += 1
            minW = min(minW, count) 
            l += 1
        return 0 if minW == float('inf') else minW