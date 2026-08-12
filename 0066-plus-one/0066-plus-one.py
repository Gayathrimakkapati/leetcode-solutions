class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str=""
        for i in range(len(digits)):
            num_str=num_str+str(digits[i])
        num_int=int(num_str)
        num_int+=1
        new_str=str(num_int)
        res=[]
        for digits in new_str:
            res.append(int(digits))
        return res
