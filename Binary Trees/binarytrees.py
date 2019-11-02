class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)


# Tree Traversal - DEPTH FIRST SEARCH(DFS)
# print all nodes on tree
def dfs(self):  # usually dfs in pre-order Treversal
    print(self.val)
    if self.left:
        self.left.dfs()
    if self.right:
        self.right.dfs()


TreeNode.dfs = dfs
t1.dfs()

# dfs in-order Traversal
print(":::::::: DFS in-order Traversal ::::::::::")


def dfs_inorder(self):
    if self.left:
        self.left.dfs()
    print(self.val)
    if self.right:
        self.right.dfs()


TreeNode.dfs_inorder = dfs_inorder
t1.dfs_inorder()

# dfs post-order Traversal
print(":::::::: DFS post-order Traversal ::::::::::")


def dfs_postorder(self):
    if self.left:
        self.left.dfs()
    if self.right:
        self.right.dfs()
    print(self.val)


TreeNode.dfs_postorder = dfs_postorder
t1.dfs_postorder()

print(":::::::: BFS Traversal ::::::::::")


def bfs(self):
    to_visit = [self]
    while to_visit:
        current = to_visit.pop(0)  # will give us value at zero index.. pop(0) gives us queue..
        print(current.val)
        if current.left:
            to_visit.append(current.left)
        if current.right:
            to_visit.append(current.right)


TreeNode.bfs = bfs
t1.bfs()

print(":::::::: Perform Arbitrary Tasks on all nodes ::::::::::")


def dfs_apply(self, fn):
    fn(self)
    if self.left:
        self.left.dfs_apply(fn)
    if self.right:
        self.right.dfs_apply(fn)


TreeNode.dfs_apply = dfs_apply


class PerfomSum:
    def __init__(self):
        self.sum = 0

    def process(self, node):
        self.sum += node.val

    def get_sum(self):
        return self.sum

    def reset_sum(self):
        self.sum = 0


p = PerfomSum()

t1.dfs_apply(p.process)
print("sum: ", p.get_sum())
p.reset_sum()   # need to reset sum, coz it adds in sum rather way..
# t1.dfs_apply(p.process)
# print(p.get_sum())
