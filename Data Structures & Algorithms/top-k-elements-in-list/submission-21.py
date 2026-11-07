#my attempt to recreate 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        reverse = [ [] for i in range(len(nums)+1)]

        for num, c in count.items():
            reverse[c].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in reverse[i]:
                res.append(n)
                if len(res) == k:
                    return res