class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = Counter(nums)
        sorted_nums = sorted([(-c,n) for n, c in counters.items()])
        return [n for (_, n) in sorted_nums[:k]]