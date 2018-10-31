
arr = []
arr_len = 10
for i in range(arr_len):
    arr.append(int(input()))

for i in range(0, arr_len - 1):
    for j in range(0, arr_len - i - 1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)