class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        i=0
        while i<len(s):
            if s[i]!=' ':
                count=0
                while i<len(s) and s[i]!=' ':
                    count+=1
                    i+=1
            else:
                i+=1
        return count