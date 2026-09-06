class Solution:
    def climbStairs(self, n: int) -> int:
        hash={}
        def dfs(curr):
            if curr==n:
                return 1
            if curr>n:
                return 0
            if curr in hash:
                return hash[curr]
            hash[curr]=dfs(curr+1)+dfs(curr+2)
            return hash[curr]
        return  dfs(0)