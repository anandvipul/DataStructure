import heapq

H = [2,3,5,3,5,6,6,43]

heapq.heapify(H)

print(H)

# Replacing an element

heapq.heapreplace(H,4)
print(H)
