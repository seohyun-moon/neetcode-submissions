class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))

        counts = []
        count = 1

        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                counts.append(count)
                count = 1
        counts.append(count)
        
        return max(counts)