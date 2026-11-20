class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m     

        n1 = nums[:l]
        n2 = nums[l:]

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
                return bs(n2, target) + l
        return -1