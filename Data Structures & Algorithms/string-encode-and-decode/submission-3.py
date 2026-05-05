class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        end = 0
        while end < len(s):
            while end < len(s) and s[end] != '#':
                end += 1
            chunk_len = int(s[start:end])
            start = end + 1
            end = end + chunk_len + 1
            res.append(s[start:end])
            start = end
        return res
