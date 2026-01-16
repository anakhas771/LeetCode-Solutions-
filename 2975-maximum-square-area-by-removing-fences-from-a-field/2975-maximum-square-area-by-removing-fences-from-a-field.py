class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        # Add boundary fences
        h = [1] + hFences + [m]
        v = [1] + vFences + [n]

        h.sort()
        v.sort()

        # Get all possible horizontal distances
        h_dist = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_dist.add(h[j] - h[i])

        # Get all possible vertical distances
        v_dist = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_dist.add(v[j] - v[i])

        # Find maximum common distance
        max_side = 0
        for d in h_dist:
            if d in v_dist:
                max_side = max(max_side, d)

        if max_side == 0:
            return -1

        return (max_side * max_side) % MOD