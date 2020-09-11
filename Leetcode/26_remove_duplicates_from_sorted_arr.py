class Solution:
    def removeDuplicates(self, nums):
        n = 0
        while n < (len(nums)-1):
            if nums[n] == nums[n+1]:
                del nums[n+1]
                n -= 1
            n +=1
        return nums

obj = Solution()
print(obj.removeDuplicates([0,0,0,0,1,2,2,2,2,2,2,2,53,545,54,54,54,843,3,3,3,3,4,5]))