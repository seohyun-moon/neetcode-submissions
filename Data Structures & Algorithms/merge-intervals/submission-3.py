# First attempt

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if res[len(res) -1][0] <= intervals[i][0] <= res[len(res) -1][1] or res[len(res) -1][1] >= intervals[i][1]:
                res[len(res) -1][0] = min(res[len(res) -1][0], intervals[i][0])
                res[len(res) -1][1] = max(res[len(res) -1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res

        