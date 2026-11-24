class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1
        for j in range(len(t)):
            countT[t[j]] += 1

        return countS == countT