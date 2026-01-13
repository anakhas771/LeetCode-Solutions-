class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #slow pointer
        i=0
        for j,n in enumerate(nums):
            if n!=nums[i]:
                i+=1
                nums[i]=n
        return i+1

        