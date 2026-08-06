
class Solution(object):
    def sortedSquares(self, nums):
        a=[int(i**2) for i in nums]
        a.sort()
        return a
       
            
obj=Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))
print(obj.sortedSquares([-7,-3,2,3,11]))
        