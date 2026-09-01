class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res= s.strip().split()
        return len(res[-1])
obj=Solution()
print(obj.lengthOfLastWord("Hello World"))
print(obj.lengthOfLastWord("   fly me   to   the moon  "))
print(obj.lengthOfLastWord("luffy is still joyboy"))