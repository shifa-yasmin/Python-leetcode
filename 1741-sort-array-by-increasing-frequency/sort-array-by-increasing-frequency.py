class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        return sorted(nums,key=lambda x:(freq[x],-x))
obj=Solution()
print(obj.frequencySort([1,1,2,2,2,3]))
print(obj.frequencySort([2,3,1,3,2]))
print(obj.frequencySort([-1,1,-6,4,5,-6,1,4,1]))