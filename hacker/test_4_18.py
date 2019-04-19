def majorityElement(nums: [int]) -> int:
    # while True:
    #     find = 0
    #     for i in range(1, len(nums)):
    #         if nums[0] != nums[i]:
    #             find = 1
    #             break
    #     if find == 0:
    #         break
    #     nums = nums[1: i] + nums[i + 1:]
    # return nums[0]
    nums.sort()
    return nums[int(len(nums)/2) - 1]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    if head == None:
        return head
    node = None
    while head != None:
        next_node = head.next
        head.next = node
        node = head
        head = next_node
    return node

def findKthLargest(nums: [int], k: int) -> int:
    largest = []
    for i in range(k):
        largest.append(nums[i])
    largest.sort()

    for j in range(k, len(nums)):
        if nums[j] > largest[0]:
            largest[0] = nums[j]
            largest.sort()
    return largest[0]

def containsDuplicate(nums: [int]) -> bool:
    set_nums = set(nums)
    if len(set_nums) == len(nums):
        return False
    return True

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthSmallest(root: TreeNode, k: int) -> int:
        values = getValues(root)
        return values[k - 1]

def getValues(root: TreeNode):
    if root == None:
        return []
    return getValues(root.left) + [root.val] + getValues(root.right)


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    # nums.sort()
    # print(nums)
    k = 2
    # print(findKthLargest(nums, k))
    print(containsDuplicate(nums))