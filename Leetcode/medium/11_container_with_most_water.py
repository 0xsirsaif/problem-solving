class Solution:
    def maxArea(self, height):
        biggest_area = 0
        for i in range(len(height)):
            for k in range(i+1,len(height)):
                tall = height[i] if (height[i] < height[k]) else height[k]
                area = tall * (k - i)
                if area > biggest_area:
                    biggest_area = area
        return biggest_area


obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))

