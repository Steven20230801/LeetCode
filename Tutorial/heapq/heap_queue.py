import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

# [1, 3, 7, 4]
heapq.nlargest(1, heap)
print(heap)
heapq.nlargest(2, heap)

heapq.nsmallest(2, heap)

list_a = [4, 1, 7, 3]
heapq.heapify(list_a)
