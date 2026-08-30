class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper() or word==word.lower() or word==word.title() and word[1:].lower():
            return True
        return False
obj=Solution()
print(obj.detectCapitalUse("USA"))
print(obj.detectCapitalUse("FlaG"))
        