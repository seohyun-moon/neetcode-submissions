class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)

        for s in s1:
            count[s] += 1

        for i in range(len(s2) - len(s1) + 1):
            count2 = defaultdict(int)
            for s in s2[i : i + len(s1)]:
                count2[s] += 1
            for s in count2.keys():
                if count2[s] != count[s]:
                    break
            else:
                return True
        
        return False