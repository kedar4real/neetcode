import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first we get the freqncy count of elements
        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
            heap=[]

        for n, cnt in count.items():
            heapq.heappush(heap,(cnt,n))


            if len(heap)>k:
                heapq.heappop(heap)
        return [num for cnt,num in heap]