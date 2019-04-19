class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    nodes_p = []
    node = root
    while node != None:
        nodes_p.append(node)
        if node.val == p.val:
            break
        elif node.val > p.val:
            node = node.left
        else:
            node = node.right
    pat = root
    node = root
    while node != None:
        if node in nodes_p:
            pat = node
        else:
            break
        if node.val == q.val:
            break
        elif node.val > q.val:
            node = node.left
        else:
            node = node.right
    return pat

def load(nums)-> TreeNode:
    l = int(len(nums)/2)
    list_node = [None for i in nums]
    head = TreeNode(nums[0])
    for i in range(l):
        if i == 0:
            head = TreeNode(nums[i])
            list_node[i] = head
        node_i = list_node[i]
        left = None
        right = None
        if 2 * i + 1 < len(nums) and nums[2 * i + 1] != None:
            left = TreeNode(nums[2 * i + 1])
        if 2 * i + 2 < len(nums) and nums[2 * i + 2] != None:
            right = TreeNode(nums[2 * i + 2])
        if node_i == None:
            continue
        node_i.left = left
        node_i.right = right
        if 2 * i + 1 < len(nums):
            list_node[2 * i + 1] = left
        if 2 * i + 2 < len(nums):
            list_node[2 * i + 2] = right
    return head


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
     pa_node = node_path(root)
     pa_path = []
     while p != None:
         pa_path.insert(0, p)
         p = pa_node.get(p)
     node = None
     while q != None:
         if p in pa_path:
             node = p
             break
     return node

def node_path(root: TreeNode):
    node = root
    pa_node = {}
    right_nodes = []
    pa_node[root] = None
    while node != None or len(right_nodes) >= 0:
        if node != None:
            if node.right != None:
                right_nodes.append(node.right)
                pa_node[node.right] = node
            if node.left != None:
                pa_node[node.left] = node
                node = node.left
            elif len(right_nodes) > 0:
                node = right_nodes.pop()
            else:
                break
    return pa_node
    pa_key = pa_node.keys()
    # for k in pa_key:
    #     node = TreeNode(k.val)
    #     pa_node[node] = pa_node.get(k)
    #     pa_node.pop(k)
    return pa_node

def reverseString(s:[str]) -> None:
    l = len(s) - 1
    for i in range(l):
        j = l - i
        if j <= i:
            break
        else:
            s[i] = s[i] + s[j]
            s[j] = s[i] - s[j]
            s[i] = s[i] - s[j]

if __name__ == '__main__':
    nums = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = TreeNode(2)
    q = TreeNode(4)
    root = load(nums)
