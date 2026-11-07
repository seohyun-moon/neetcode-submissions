class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, recolor, res = 0, 0, k

        for r in range(len(blocks)):
            if blocks[r] == "W":
                recolor += 1
            if (r-l+1) == k:
                res = min(recolor, res)
                if blocks[l] == "W":
                    recolor -= 1
                l += 1
        return res