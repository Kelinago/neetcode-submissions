from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = Counter(nums)
        min_heap = []
        for n, c in counters.items():
            heappush(min_heap, (c, n))
            if len(min_heap) > k:
                heappop(min_heap)
        return [heappop(min_heap)[1] for _ in range(k)]