class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 1
        f = sorted(citations, reverse=True)
        for i, num in enumerate(f, start=1):
            if i > num:
                h = i - 1
                break
            else:
                h = len(citations)
        return h