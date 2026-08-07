class Solution(object):
    def isAnagram(self, s, t):
        if sorted(s)==sorted(t):
           return True
        else:
            return False
obj=Solution()
print(obj.isAnagram("anagram","nagaram"))
print(obj.isAnagram("rat","car"))

        