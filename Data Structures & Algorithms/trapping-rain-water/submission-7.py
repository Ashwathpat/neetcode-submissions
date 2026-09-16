class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        leftmax=height[l]
        rightmax=height[r]

        if not height:
            return 0

        while l<r:
            if leftmax<rightmax:
                #move the left pointer
                l+=1
                #update leftmax if bigger
                leftmax=max(leftmax,height[l])
                #return 
                res+=leftmax-height[l]
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                res+=rightmax-height[r]
        return res