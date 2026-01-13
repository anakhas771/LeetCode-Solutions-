class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        
        # Step 2: Vertical scanning using enumerate
        for i, ch in enumerate(shortest):
            for s in strs:
                if s[i] != ch:  # Stop at first mismatch
                    return shortest[:i]
        
        # Step 3: All characters matched
        return shortest

        