
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    left = merge_sort(arr[n//2:])
    right = merge_sort(arr[:n//2])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result



if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    print(test_arr)
    sorted_arr = merge_sort(test_arr)
    print(sorted_arr)

    test_arr.sort(reverse=True)
    print(test_arr)
    print(merge_sort(test_arr))

    for i, j in zip(sorted_arr, [1, 1, 2, 3, 6, 8, 10]):
        if i != j:
            print("DINT WORK")
