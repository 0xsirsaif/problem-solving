# class Solution:
#     def maxArea(self, height):
#         mid_ele = len(height)//2
#         biggest_area = (len(height) - mid_ele -1) * (height[mid_ele] if (height[mid_ele] < height[len(height)-1]) else height[len(height)-1])
#         for i in range(len(height)):
#             far_ele = (len(height)-1) if (i < mid_ele) else (0)
#             tall = height[i] if (height[i] < height[far_ele]) else height[far_ele]
#             area = tall * abs(far_ele - i)
#             if area > biggest_area:
#                     biggest_area = area


class Solution:
    def maxArea(self, height):
        mid_ele = len(height) // 2
        biggest_area = (len(height) - mid_ele - 1) * (height[mid_ele] if (height[mid_ele] < height[len(height)-1]) else height[len(height)-1])
        for i in range(len(height)):
            print("ele: ", height[i])
            far_ele = (len(height) - 1) if (i < mid_ele) else (0)
            tall = height[i] if (height[i] < height[far_ele]) else height[far_ele]
            area_1 = tall * abs(far_ele - i)

            height_ele = max(enumerate(height), key=lambda item: item[1])[0]
            tall = height[i] if (height[i] < height[height_ele]) else height[height_ele]
            area_2 = tall * abs(height_ele - i)
            print("far_ele:", far_ele, "height_ele:", height[height_ele])
            print("area_1: ",area_1, "area_2: ",area_2)
            biggest_area = max(area_1, area_2, biggest_area)
            print("================")
        return biggest_area




obj = Solution()
print(obj.maxArea([75,21,3,152,13,107,163,166,32,160,41,131,7,67,56,5,153,176,29,139,61,149,176,142,64,75,170,156,73,48,148,101,70,103,53,83,11,168,1,195,81,43,126,88,62,134,45,167,63,26,107,124,128,83,67,192,158,189,149,184,37,49,85,107,152,90,143,115,58,144,62,139,139,189,180,153,75,177,121,138,4,28,15,132,63,82,124,174,23,25,110,60,74,147,120,179,37,63,94,47]))

# class Solution:
#     def maxArea(self, height, area, n):
#         biggest_area = area
#         n = n
#         if n > len(height):
#             return biggest_area
#         else:
#             for k in range(n,len(height)):
#                 tall = height[n] if (height[n] < height[k]) else height[k]
#                 area = tall * (k - n)
#                 if area > biggest_area:
#                     biggest_area = area
#         return self.maxArea(height, biggest_area, n+1)

class SolutionB:
    def maxArea(self, height):
        biggest_area = 0
        for i in range(len(height)):
            for k in range(i+1,len(height)):
                tall = height[i] if (height[i] < height[k]) else height[k]
                area = tall * (k - i)
                if area > biggest_area:
                    biggest_area = area
                    print(height[i],height[k])
        return biggest_area

print("#####################################################3")
obj = SolutionB()
print(obj.maxArea([75,21,3,152,13,107,163,166,32,160,41,131,7,67,56,5,153,176,29,139,61,149,176,142,64,75,170,156,73,48,148,101,70,103,53,83,11,168,1,195,81,43,126,88,62,134,45,167,63,26,107,124,128,83,67,192,158,189,149,184,37,49,85,107,152,90,143,115,58,144,62,139,139,189,180,153,75,177,121,138,4,28,15,132,63,82,124,174,23,25,110,60,74,147,120,179,37,63,94,47]))
