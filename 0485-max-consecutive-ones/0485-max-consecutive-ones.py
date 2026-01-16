class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxcount=0
        for i in nums:
            if i==1:
                count+=1
                maxcount=max(count,maxcount)
            else:
                count=0
        return maxcount
