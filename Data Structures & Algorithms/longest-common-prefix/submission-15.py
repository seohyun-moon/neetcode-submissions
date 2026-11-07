class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # think of it as a matrix
        # visit row -> col        
        prefix = strs[0]
        for x in range(1, len(strs)):
            y = 0
            while y < min(len(prefix), len(strs[x])):
                if prefix[y] != strs[x][y]:
                    break
                y += 1
            prefix = prefix[:y]
        return prefix