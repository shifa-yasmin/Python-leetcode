class Solution(object):
    def detectCapitalUse(self, word):
        for i in word:
            if  word.isupper() or word.islower() or word[0].isupper() and word[1:].islower():
                return True
            else:
                return False
obj=Solution()
print(obj.detectCapitalUse("USA"))
print(obj.detectCapitalUse("FlaG"))