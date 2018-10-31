arr = []
arr_len = 10
for i in range(arr_len):
    arr.append(int(input()))

for i in range(1, arr_len):
    temp = arr[i]
    j = i
    while j > 0:
        if arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        else:
            break
    arr[j] = temp

print(arr)