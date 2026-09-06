class Solution:
    def rob(self, nums: List[int]) -> int:
        hash={}
        def dfs(i):
            if i>=len(nums):
                return 0
            if i in hash:
                return hash[i]
            hash[i]=max(dfs(i+1),nums[i]+dfs(i+2))
            return hash[i]
        return dfs(0)
        