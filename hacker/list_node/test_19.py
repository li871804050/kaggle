# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rightSideView(self, root: TreeNode) -> [int]:
    if root == None:
        return []
    res = {}
    nodes = []
    deep_map = {}
    deep = 0
    while True:
        if root == None:
            if len(nodes) == 0:
                break
            root = nodes.pop()
            deep = deep_map.get(root)
        else:
            if deep not in res.keys():
                res[deep] = root.val
            nodes.append(root.left)
            deep += 1
            deep_map[root.right] = deep
            deep_map[root.left] = deep
            root = root.right
    return res.values()

def add(nums):
    if len(nums) == 0:
        return None
    root = TreeNode(nums[0])
    nodes = []
    nodes.append(root)
    for i in range(1, len(nums)):
        if nums[i] != None:
            new_node = TreeNode(nums[i])
            nodes.append(new_node)
        else:
            new_node = "None"
        node = nodes[0]
        if node.left == None:
            node.left = new_node
            continue
        if node.right == None:
            node.right = new_node
            nodes.pop(index=0)
    return root
