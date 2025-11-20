
class Node:
    def __init__(self, key, val):
        pass


class MyHashMap:

    def __init__(self, size=4):
        pass

    def add(self, key, value):
        pass

    def remove(self, key):
        pass

    def get(self, key):
        pass


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

