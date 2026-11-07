class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, sum = 0, 0
        min_length = float("inf")

        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                min_length = min(min_length, r-l+1)
                sum -= nums[l]
                l += 1
        return 0 if min_length == float("inf") else min_length