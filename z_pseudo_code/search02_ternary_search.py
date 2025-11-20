
class TernarySearch:

    def __init__(self, arr):
        self.arr = arr

    def search(self, key):
        pass


if __name__ == "__main__":
    test_arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    obj = TernarySearch(test_arr)
    print(obj.search(5))
    for i in test_arr:
        print(obj.search(i))
