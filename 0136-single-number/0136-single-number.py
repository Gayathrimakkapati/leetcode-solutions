class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for e in nums:
            if e in d:
                d[e]+=1
            else:
                d[e]=1
        for k,v in d.items():
            if v==1:
                return k