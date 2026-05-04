class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = Counter(nums)
        sorted_nums = sorted([(-v,k) for k, v in counters.items()])
        return [k for (v, k) in sorted_nums[:k]]