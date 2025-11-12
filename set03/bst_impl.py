
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, val: int, cur_root=None):

        if not cur_root:
            if not self.root:
                self.root = Node(val)
                return
            else:
                cur_root = self.root

        if val <= cur_root.val:
            if not cur_root.left:
                cur_root.left = Node(val)
            else:
                self.add(val, cur_root.left)
        else:
            if not cur_root.right:
                cur_root.right = Node(val)
            else:
                self.add(val, cur_root.right)

    def print(self, cur_root=None):
        if not cur_root:
            cur_root = self.root

        if cur_root:
            if cur_root.left:
                self.print(cur_root.left)
            print(cur_root.val)
            if cur_root.right:
                self.print(cur_root.right)


if __name__ == "__main__":
    arr = [8, 3, 10, 1, 14, 6, 4, 7, 13]
    obj = BST()
    for i in arr:
        obj.add(i)
    obj.print()
