def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap elements
    return arr

# User input
input_str = input("")
input_list = [int(x) for x in input_str.split(',')]

# Sort and print the list
print(bubble_sort(input_list))