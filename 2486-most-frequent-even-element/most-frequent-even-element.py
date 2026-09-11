class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res={}
        for i in nums:
            if i%2==0:
                res[i]=res.get(i,0)+1
        if not res:
            return -1       
        count=max(res.values())
        return min(i for i in res if res[i]==count)