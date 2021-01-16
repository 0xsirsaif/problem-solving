from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Do not return anything, modify nums1 in-place instead."""
        def right_shift(idx):
            prev_item = nums1[idx]
            for i in range(idx, initial_arr_len):
                temp = nums1[i]
                nums1[i] = prev_item
                prev_item = temp

        if m == 0:
            nums1 = nums2
            print(nums1, "???")
            return
        initial_arr_len = len(nums1)

        ptr_1 = ptr_2 = 0
        while ptr_1 < m and ptr_2 < n:
            if nums1[ptr_1] > nums2[ptr_2]:
                right_shift(ptr_1)
                nums1[ptr_1] = nums2[ptr_2]
                ptr_2 += 1
            elif nums2[ptr_2] > nums1[ptr_1]:
                ptr_1 += 1
            else:
                right_shift(ptr_1)
                nums1[ptr_1] = nums2[ptr_2]
                ptr_1 += 1
                ptr_2 += 1
        if n > ptr_2 + 1:
            nums1[ptr_1+1:] = nums2[ptr_2:]

        print(nums1)

s = Solution()
print(s.merge(nums1=[0], m=0, nums2=[1], n=1))
