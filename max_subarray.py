#Used kadanes Algorithm to solve this subarray problem

class Solution:
    def maxSubArray(self, nums):
        maxsodar=nums[0]
        currentsum=nums[0]
        for i in range(1,len(nums)):
            if (currentsum<0):
                currentsum=0
            currentsum+=nums[i]
            if currentsum>maxsodar:
                maxsodar=currentsum
        return maxsodar