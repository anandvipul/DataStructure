import heapq

H = [21, 2, 1, 45, 78, 3, 5]

# Creating the heap H

heapq.heapify(H)
print('Heap H', H)


# Remove element from the heap

heapq.heappop(H)

print(H)
