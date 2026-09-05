class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        s1count=[0]*26
        s2count=[0]*26

        if n1>n2:return False

        #updating hash array for s1

        for i in range(n1):
            s1count[ord(s1[i])-ord('a')]+=1
            s2count[ord(s2[i])-ord('a')]+=1
        
        if s1count==s2count:return True

        #sliding window

        for i in range(n1,n2):
            s2count[ord(s2[i])-ord('a')]+=1
            s2count[ord(s2[i-n1])-ord('a')]-=1
            if s1count==s2count:return True

        return False

