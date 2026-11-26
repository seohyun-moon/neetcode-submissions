class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [c.lower() for c in s if c.isalnum()]

        l, r = 0, len(clean) - 1
        while l < r:
            if clean[l] == clean[r]:
                l = l + 1
                r = r - 1
            else:
                return False
        return True