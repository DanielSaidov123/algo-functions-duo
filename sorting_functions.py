def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    smaller = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
     numbers = [64, 34, 25, 12, 22, 11, 90]
     print(bubble_sort(numbers))
     print(quick_sort(numbers))

