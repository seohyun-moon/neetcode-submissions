class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            m = (l+r) // 2
            T = 0
            for i in range(len(piles)):
                if piles[i] % m == 0:
                    T += piles[i] // m
                else:
                    T += piles[i] // m + 1
            if T <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res