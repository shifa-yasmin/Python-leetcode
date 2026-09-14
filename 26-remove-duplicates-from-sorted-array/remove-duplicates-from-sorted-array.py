class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            if i not in res:
                res.append(i)
        for i in range(len(res)):
            nums[i]=res[i]
        return len(res)