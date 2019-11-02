class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


def dfs(self):  # usually dfs in pre-order Traversal
    print(self.val)
    if self.left:
        self.left.dfs()
    if self.right:
        self.right.dfs()


TreeNode.dfs = dfs


def dfs_inorder(self):
    if self.left:
        self.left.dfs()
    print(self.val)
    if self.right:
        self.right.dfs()


TreeNode.dfs_inorder = dfs_inorder


class BST(TreeNode):
    def __init__(self, val, parent=None):
        super().__init__(val)
        self.parent = parent

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                new_node = BST(val, parent=self)
                self.left = new_node
            else:
                self.left.insert(val)
        else:  # greater
            if self.right is None:
                self.right = BST(val, parent=self)
            else:
                self.right.insert(val)


def find_root(self):
    """Find the absolute root of BST to which self belongs.."""
    temp = self
    while temp.parent is not None:
        temp = temp.parent
    return temp
    # Keep going until no parent .... return that


BST.find_root = find_root


def find_min(self):
    """Find the minimum value starting from self.
    IN BST, this is simple, keep going left until no left is left"""
    min_node = self
    if self.left is not None:
        min_node = self.left.find_min()
    return min_node


BST.find_min = find_min


def set_for_parent(self, new_ref):
    """Disconnect self from parent and attach new_ref to parent in self's place"""
    if self.parent is None: return

    if self.parent.right == self:
        self.parent.right = new_ref
    if self.parent.left == self:
        self.parent.left = new_ref


BST.set_for_parent = set_for_parent


def replace_with_node(self, node):
    """Replace self with node (Which is child). Make sure to fix the parent of the node and parent' pointing to node.
    Assume we have no children other than node"""
    self.set_for_parent(node)  # Connect new node to parent on proper location
    node.parent = self.parent  # Set node's parent correctly
    self.parent = None  # Disconnect self from the parent
    return node.find_root()


BST.replace_with_node = replace_with_node


def delete(self, val):
    # first... if we are alone, on the root and no children plus the value matches, just return None
    if self.parent is None and self.right is None and self.left is None and self.val == val:
        return None
    # We are the node to be deleted
    if self.val == val:
        # Check if we are lead
        if self.right is None and self.left is None:
            self.set_for_parent(None)  # Set in place of self a None
            return self.find_root()

        # Check if we have just a left node
        if self.right is None:
            return self.replace_with_node(self.left)

        # Check if we have just a right node
        if self.left is None:
            return self.replace_with_node(self.right)

        # Now we have both Children. Find the Successor and replace "self" with it.
        """(Our Successor is definitely in our right child and it can't have two children 
        because left child will always be smaller)"""
        successor = self.right.find_min()
        # Copy successor's val here
        self.val = successor.val

        return self.right.delete(successor.val)
        # ^ delete the successor node, which is our right child BST.
        # ^ It is guaranteed that it's the simpler case since successor CANNOT have a left child.
    # We were not the node to be deleted, go to children
    if val < self.val:
        if self.left:
            return self.left.delete(val)
        else:
            return self.find_root()  # Nothing to delete
    else:
        if self.right:
            return self.right.delete(val)
        else:
            return self.find_root()


BST.delete = delete

b = BST(20)
# print(b.val)
b.insert(13)
b.insert(10)
b.insert(155)
b.insert(12)
# print(b.dfs())
print(":::::::: DFS in-order Traversal ::::::::::")
# print(b.dfs_inorder())
# print(b.left.find_min().val)
b = b.delete(20)
b = b.delete(155)
# print(":::::::: ISSUE WITH THE BST - BALANCE ::::::::::")
# # l = [1, 2, 4, 9, 13, 21, 51, 71, 82]
# # a = BST(l[0])
# # for i in l[1:]:
# #     a.insert(i)
# #
# # print(a.dfs_inorder())
# If you insert values in specific way in BST, All the advantages of BST finishes..

