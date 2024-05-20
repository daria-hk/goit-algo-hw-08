import heapq

def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    
    return [heapq.heappop(h) for _ in range(len(h))]

def heap_sort_desc(iterable):
    h = []

    for value in iterable:
        heapq.heappush(h, -value)
    
    return [-heapq.heappop(h) for _ in range(len(h))]

# Array to sort
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
sorted_arr_desc = heap_sort_desc(arr)

print("Sorted array by growth:", sorted_arr)

sum = 0

for i in range(len(sorted_arr)):
    sum += sorted_arr[i]
    print(sum)

print("Sorted array in descending order:", sorted_arr_desc)

sum_for_desc = 0

for i in range(len(sorted_arr_desc)):
    sum_for_desc += sorted_arr_desc[i]
    print(sum_for_desc)

print("Conclusions: min heap minimizes total costs")
