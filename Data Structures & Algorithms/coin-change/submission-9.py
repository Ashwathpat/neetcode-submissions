class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hash={}
        def dfs(curr):
            if curr==amount:
                return 0
            if curr>amount:
                return float('inf')
            if curr in hash:
                return hash[curr]
            mincoin=float('inf')
            for coin in coins:
                mincoin=min(mincoin,1+dfs(curr+coin))
            hash[curr]=mincoin
            return hash[curr]
        ans=dfs(0)
        if ans!=float('inf'):
            return ans
        else :return -1
        