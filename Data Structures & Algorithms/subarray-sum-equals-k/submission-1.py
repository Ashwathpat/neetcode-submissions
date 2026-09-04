class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        hash={}
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            if total==k:
                count+=1
            if (total-k) in hash:
                count+=hash[total-k]
            if total in hash:
                hash[total]+=1
            else:
                hash[total]=1
        return count
        