class Solution(object):
    def isPalindrome(self, s):
        res=""
        for ch in s:
            if ch.isalnum():
               res+=ch.lower()
        if res==res[::-1]:
            return True
        else:
            return False

obj=Solution()   
print(obj.isPalindrome("A man, a plan, a canal: Panama")) 
print(obj.isPalindrome("race a car")) 
print(obj.isPalindrome(" ")) 