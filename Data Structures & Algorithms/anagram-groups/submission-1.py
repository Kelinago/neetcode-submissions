class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key: hash of string representing number of every chars, val: list of strings
        result = defaultdict(list)
        for s in strs:
            s_hash = ''.join(
                f'{v}{k}'
                for k, v in sorted(Counter(s).items())
            )
            result[s_hash].append(s)
        return list(result.values())