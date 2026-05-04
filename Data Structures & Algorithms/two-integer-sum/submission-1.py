class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: diff with target, value: index in nums
        pair_dict = defaultdict(int)
        for i, n in enumerate(nums):
            diff = target - n
            if diff in pair_dict:
                return [pair_dict[diff], i]
            pair_dict[n] = i

        return []
