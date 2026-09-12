class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        majority=0
        for i in nums:
            freq[i]=freq.get(i,0)+1
            if freq[i]> len(nums) /2:
                return i
