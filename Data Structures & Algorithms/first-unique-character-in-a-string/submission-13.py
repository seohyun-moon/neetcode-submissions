class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hash map: count the number of alphabets
        count = defaultdict(int)

        for c in s:
            count[c] += 1

        # return the first key with the value ot 1
        ones = []
        for c in count:
            if count[c] == 1:
                ones.append(c)

        # return it's index
        if not ones:
            return -1
        return s.index(ones[0])