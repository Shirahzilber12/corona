from AppData.Local.Programs.Python.Python36.Lib import heapq


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

def heapsort2(iterable):
    h = []
    heapq._heapify_max(h)
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

if __name__ == "__main__":

    # print(heapsort([1, 3,232, 5, 7, 9, 2, 4, 6, 8, 0]))
    print (heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))