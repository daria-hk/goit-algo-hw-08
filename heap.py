import heapq

def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    
    return [heapq.heappop(h) for _ in range(len(h))]

# Array to sort
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)

print("Sorted array by growth:", sorted_arr)

sum = 0

for i in range(len(sorted_arr)):
    sum += sorted_arr[i]
    if i == 0:
        print(f"{sum} {sorted_arr[i+1:]}")
    else:
        print(f"{sorted_arr[i-1]} + {sorted_arr[i]} = {sum}   {sorted_arr[i+1:]}")

print("Min costs =", sum)


