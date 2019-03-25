class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def check_binary_search_tree_(root):
    check = check_binary_search_tree_2(root)
    if check:
        return 'Yes'
    else:
        return 'No'

def check_binary_search_tree_2(root):
    if root.left != None and root.right != None:
        if root.left.data > root.data or root.right.data < root.data:
            return False
        else:
            return check_binary_search_tree_2(root.right) and check_binary_search_tree_2(root.left)
    elif root.left != None:
        if root.left.data > root.data:
            return False
        else:
            return check_binary_search_tree_2(root.left)
    elif root.right != None:
         if root.right.data < root.data:
            return False
         else:
            return check_binary_search_tree_2(root.right)
    else:
        return True