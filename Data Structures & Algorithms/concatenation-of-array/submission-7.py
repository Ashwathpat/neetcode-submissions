class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newstr=[]
        for i in range(2):
            for num in nums:
                newstr.append(num)
        return newstr
        
