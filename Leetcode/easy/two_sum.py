class Solution:
    def twoSum(self, nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return [nums_dict[nums[i]], i]
            else:
                nums_dict[target-nums[i]] = i
s = Solution()
print(s.twoSum([3,2,3], 6))


# nums2 = sorted(nums)
        # for i in range(len(nums2)):
        #     for k in range(len(nums2)):
        #         if nums2[k] == target - nums2[i]:
        #             return [nums.index(nums2[i]), nums.index(nums2[k])+1]
        #         elif nums2[k] > target - nums2[i]:
        #             break
# =========================================
# result = []
        # def get_indices(curr_val):
        #     for k in range(len(nums)):
        #         if i == k:
        #             continue
        #         elif curr_val == target-nums[k]:
        #           result.append(i)
        #           result.append(k)
        #
        # for i in range(len(nums)):
        #     curr_val = nums[i]
        #     if curr_val <= target:
        #         get_indices(curr_val)
        #
        # mid_result = len(result) // 2
        # print(result[0:mid_result])
        # return result[0:mid_result]