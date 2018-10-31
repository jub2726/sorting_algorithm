arr = []
arr_len = 10
for i in range(arr_len):
    arr.append(int(input()))

def merge_sort(low, high):
    global arr
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid + 1, high)

        i = low
        j = mid + 1
        arr2 = []
        while i <= mid and j <= high:
            if arr[i] < arr[j]:
                arr2.append(arr[i])
                i += 1
            else:
                arr2.append(arr[j])
                j += 1
        while i <= mid:
            arr2.append(arr[i])
            i += 1
        while j <= high:
            arr2.append(arr[j])
            j += 1
        k = 0
        for m in range(low, high + 1):
            arr[m] = arr2[k]
            k += 1

merge_sort(0, arr_len-1)
print(arr)