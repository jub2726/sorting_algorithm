arr = []
arr_len = 10
for i in range(arr_len):
    arr.append(int(input()))

for i in range(0, arr_len - 1):
    min = arr[i]
    min_index = i
    for j in range(i + 1, arr_len):
        if min > arr[j]:
            min = arr[j]
            min_index = j
    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

print(arr)