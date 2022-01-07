import sys


nums1 = list(sys.stdin.readline().strip())
nums2 = list(sys.stdin.readline().strip())

print(list(nums1), list(nums2))

def find_median(nums1, nums2):
    median = 0
    if(0 < len(nums1) < 1000 and 0 < len(nums2) < 1000 and 1 <= len(nums1 + nums2) <= 2000):
        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)
        if(length > 1):
            if(length % 2 != 0):
                median = nums3[length//2]
            elif(len(nums3) % 2 == 0):
                median = (nums3[length//2 - 1] + nums3[length//2])/2
        else:
            median = nums3[0]
        return median

print(find_median(list(nums1), list(nums2)))
