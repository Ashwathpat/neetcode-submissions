class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=0
        while l<len(s)//2:
            temp=s[l]
            s[l]=s[len(s)-1-l]
            s[len(s)-1-l]=temp
            l+=1