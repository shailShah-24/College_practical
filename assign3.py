# You are given an integer array height of length n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0) and
# (i, height[i]). Find two lines that together with the x-axis
# form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store. Notice that you may
# not slant the container.
def maxArea(A, Len) :
    area = 0
    for i in range(Len) :
     for j in range(i + 1, Len) :
         # Calculating the max area
         area = max(area, min(A[j], A[i]) * (j - i))
    return area



a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
b = [1, 1]

len1 = len(a)
print(maxArea(a, len1))

len2 = len(b)
print(maxArea(b, len2))
