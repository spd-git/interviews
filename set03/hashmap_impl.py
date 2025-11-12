
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self, size=4):
        self.size = size
        self.bucket: [Node or None] = [None] * size

    def _get_hash(self, key) -> int:
        return len(key) % self.size

    def add(self, key, value):
        index = self._get_hash(key)

        if not self.bucket[index]:
            self.bucket[index] = Node(key, value)
        else:
            tmp_node = self.bucket[index]
            while tmp_node.next and not tmp_node.key == key:
                tmp_node = tmp_node.next

            if tmp_node.key == key:
                tmp_node.val = value
            else:
                tmp_node.next = Node(key, value)

    def remove(self, key):
        node = self.get(key)
        if node:
            index = self._get_hash(key)
            tmp_node = self.bucket[index]
            prev_node = None
            while tmp_node != node:
                prev_node = tmp_node
                tmp_node = tmp_node.next
            if prev_node:
                prev_node.next = tmp_node.next
            else:
                self.bucket[index] = tmp_node.next
            del tmp_node
        return None

    def get(self, key):
        index = self._get_hash(key)
        if not self.bucket[index]:
            return None
        else:
            tmp_node = self.bucket[index]
            while tmp_node.next and not tmp_node.key == key:
                tmp_node = tmp_node.next

            if tmp_node.key == key:
                return tmp_node
            else:
                return None


if __name__ == "__main__":
    obj = MyHashMap(4)
    obj.add("Sudeep", "10345")
    obj.add("Sudeep", "10346")
    obj.add("Shuchi", "10363")
    obj.add("Suhaan", "10001")

    # obj.remove("Sudeep")
    obj.remove("Shuchi")
    # obj.remove("Suhaan")
    print(obj.get("Sudeep").val)

