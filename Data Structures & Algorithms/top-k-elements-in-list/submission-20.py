class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        res = []

        for _ in range(k):
            best = None
            for num in count:
                if best == None or count[num] > count[best]:
                    best = num
            res.append(best)
            del count[best]
        
        return res