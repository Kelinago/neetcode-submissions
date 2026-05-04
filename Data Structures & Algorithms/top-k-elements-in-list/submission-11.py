from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = [[] for _ in range(len(nums) + 1)]
        for num, count in Counter(nums).items():
            freq_map[count].append(num)
        res = []
        for i in range(len(freq_map) - 1, 0, -1):
            for num in freq_map[i]:
                res.append(num)
                if len(res) == k:
                    return res