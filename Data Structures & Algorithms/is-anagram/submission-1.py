class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.replace(" ","").lower()
        t.replace(" ","").lower()
        return sorted(s)==sorted(t)