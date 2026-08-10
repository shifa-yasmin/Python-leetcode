class Solution(object):
    def getLeastFrequentDigit(self, n):
        freq={}
        
        for i in str(n):
            freq[i]=freq.get(i,0)+1
        res= min(freq,key=lambda x:(freq[x],x))
        return int(res)
obj=Solution()
print(obj.getLeastFrequentDigit(1553322))
print(obj.getLeastFrequentDigit(723344511))
        