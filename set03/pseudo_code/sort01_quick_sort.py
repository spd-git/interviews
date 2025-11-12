
def quick_sort_recursive(arr: [int]):
    pass


if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort_recursive(test_arr)
    print(sorted_arr)
    for i, j in zip(sorted_arr, [1, 1, 2, 3, 6, 8, 10]):
        if i != j:
            print("DINT WORK")
