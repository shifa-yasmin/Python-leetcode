
class Solution(object):
    def capitalizeTitle(self, title):
        res=title.split()
        ans=[]
        for i in res:
            if len(i)<=2:
                ans.append(i.lower())
            else:
                ans.append(i.capitalize())
        return " ".join(ans)
obj=Solution()
print(obj.capitalizeTitle("capiTalIze tHe titLe"))
print(obj.capitalizeTitle("First leTTeR of EACH Word"))
print(obj.capitalizeTitle("i lOve leetcode"))
        