import heapq

H = [21, 1, 45, 78, 3, 5]

# Convert to a heap

heapq.heapify(H)
print(H)

# Add element

heapq.heappush(H,8)

print(H)
