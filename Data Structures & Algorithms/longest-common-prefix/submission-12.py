class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for col in range(len(strs[0])):
            ch = strs[0][col]
            for word in strs[1:]:
                if col >= len(word) or word[col] != ch:
                    return strs[0][:col]
        return strs[0]