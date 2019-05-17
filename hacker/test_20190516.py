class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        i = 0
        c = 0
        while i < len(nums):
            if nums[i] == nums[c]:
                if i - c > 1:
                    nums.pop(i)
                    i -= 1
            else:
                c = i
            i += 1
        return len(nums)

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        node = head
        last_node = None
        while node != None:
            find_same = False
            while node.next != None and node.val == node.next.val:
                find_same = True
                node = node.next
            if last_node == None and find_same:
                head = node.next
            elif last_node != None and not find_same:
                last_node.next = node
                last_node = node
            elif last_node == None and not find_same:
                last_node = node
            elif last_node != None and find_same:
                if node.next == None:
                    last_node.next = None
            node = node.next
        return head

    def addListNode(self, nums):
        for i in range(len(nums)):
            if i == 0:
                head = ListNode(nums[i])
                node = head
            else:
                n_node = ListNode(nums[i])
                node.next = n_node
                node = n_node
        return head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        node = head
        while node != None:
            if node.next != None and node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head

    def maximalRectangle(self, matrix: [[str]]) -> int:
        if len(matrix) == 0:
            return 0

    def largestRectangleArea(self, heights: [int]) -> int:
        if len(heights) == 0:
            return 0
        res = []
        for i in range(len(heights)):
            m = 0
            for j in range(i, len(heights)):
                s = min(heights[i: j + 1])*(j + 1 - i)
                if s > m:
                    m = s
            res.append(m)
        return max(res)



if __name__ == '__main__':
    soultion = Solution()
    # nums = [1, 1, 1, 2, 2, 3]
    # print(soultion.removeDuplicates(nums))
    # nums = [1,2,2]
    # head = soultion.addListNode(nums)
    # root = soultion.deleteDuplicates(head)
    # print(root)