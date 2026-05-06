class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [4  2  3  5 ]
        # [1  4  8 24 ]
        # [30 15 5  1 ]
        # [30 60 40 24 ]
        asc = [1 for _ in nums]
        desc = [1 for _ in nums]
        for i in range(1, len(nums)):
            asc[i] = nums[i - 1] * asc[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            desc[i] = nums[i + 1] * desc[i + 1]
        return [
            asc[i] * desc[i]
            for i in range(len(nums))
        ]
