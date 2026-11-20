class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def findBreak(nums:List[int], target: int) -> int:
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[r] < nums[m]:
                    l = m + 1
                elif nums[r] > nums[m]:
                    r = m
            return l
        
        m = findBreak(nums, target)

        n1 = nums[:m]
        n2 = nums[m:]

        def bs(nums: List[int], target: int) -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m -1
                else:
                    return m
            return -1
        
        if bs(n1, target) != -1:
            return bs(n1, target)
        else:
            if bs(n2, target) != -1:
                return bs(n2, target) + m
        return -1