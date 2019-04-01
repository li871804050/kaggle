def findMedianSortedArrays(nums1, nums2) -> float:
    l1 = 0
    l2 = 0
    num = []
    l = len(nums1) + len(nums2)
    while True:
        if l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] <= nums2[l2]:
                num.append(nums1[l1])
                l1 += 1
            else:
                num.append(nums2[l2])
                l2 += 1
        elif l1 == len(nums1):
            num.append(nums2[l2])
            l2 += 1
        elif l2 == len(nums2):
            num.append(nums1[l1])
            l1 += 1
        if len(num) - 1 >= int(l / 2):
            if l % 2 == 0:
                return (num[int(l / 2)] + num[int(l / 2 - 1)]) / 2
            else:
                return num[int((l - 1) / 2)]

if __name__ == '__main__':
    num1 = [1, 2]
    num2 = [3, 4]
    print(findMedianSortedArrays(num1, num2))