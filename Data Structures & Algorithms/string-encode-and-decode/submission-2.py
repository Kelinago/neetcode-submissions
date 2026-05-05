class Solution:
    def encode(self, strs: List[str]) -> str:
        return ','.join([str(len(strs))] + [
            f'{s.encode().hex()}'
            for s in strs
        ])

    def decode(self, s: str) -> List[str]:
        chunks = s.split(',')
        if len(chunks) <= 1:
            return []
        return [
            bytes.fromhex(chunk).decode()
            for chunk in chunks[1:]
        ]
