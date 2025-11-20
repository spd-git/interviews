
arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]
 
class Node:
    value = 0
    right = None
    left = None
    height = None

    def __init__(self, value, height):
        self.value = value
        self.height = height

class BST:

    root = None
    height = -1

    def __init__(self):
        pass

    def insert(self, value):
        if self.root == None:
            self.root = Node(value, self.height + 1)
            self.height = self.height + 1
        else:
            cur = self.root
            parent = None
            h = 0
            while cur != None:
                if cur.value < value:
                    if cur.right == None:
                        cur.right = Node(value, h + 1)
                        h = h + 1
                        break
                    cur = cur.right
                else:
                    if cur.left == None:
                        cur.left = Node(value, h + 1)
                        h = h + 1
                        break
                    cur = cur.left
                h = h + 1
            if h > self.height:
                self.height = h

    def delete(self):
        pass

    def search(self):
        pass

    def print_tree(self, current):
        if current == None:
            return
        print(current.value, current.height)
        self.print_tree(current.left)
        self.print_tree(current.right)

    def print_subtree(self):
        pass

    def print_left_face(self, current, height, height_map):
        if current == None:
            return
        if height == current.height and height_map[height] == 0:
            print(current.value)
            height_map[height] = 1
        self.print_left_face(current.left, height + 1, height_map)
        self.print_left_face(current.right, height + 1, height_map)

    def create_from_array(self, arr):
        for x in arr:
            self.insert(x)
 
bst = BST()
bst.create_from_array(arr)
h_map = [0 for i in range(bst.height+1)]
bst.print_left_face(bst.root, 0, h_map)
