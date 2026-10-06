class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1# start from the first element as 0th element is already sorted
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l
        

 
        