class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        final=[]
        res= s1.split()
        res1=s2.split()
        result=res+res1
        count={}
        for i in result:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i in count:
            if count[i]==1:
                final.append(i)
        return final




            
obj=Solution()
print(obj.uncommonFromSentences("this apple is sweet","this apple is sour"))
print(obj.uncommonFromSentences("apple apple","banana"))
