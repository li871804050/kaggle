class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        node = head
        insertNode = None
        last = None
        while node != None:
            if node.val < x:
                if insertNode == None:
                    if last != None:
                        last.next = node.next
                        last = node
                    insertNode = node
                    next = head.next
                    nextNode = node.next
                    node.next = next
                    insertNode.next = head
                    head = insertNode
                    node = nextNode
                else:
                    last.next = node.next
                    next = node.next
                    node.next = insertNode.next
                    insertNode.next = node
                    insertNode = node
                    last = node
                    node = next
            else:
                last = node
                node = node.next
        return head

def addList(list):
    head = None
    node = None
    for l in list:
        if head == None:
            head = ListNode(l)
            node = head
        else:
            node.next = ListNode(l)
            node = node.next
    return head

def printNode(head):
    node = head
    while node != None:
        print(node.val,)
        node = node.next

if __name__ == '__main__':
    l = [1,4,3,2,5,2]
    nodes = addList(l)
    # printNode(nodes)
    s = Solution()
    res = s.partition(nodes, 3)
    printNode(res)