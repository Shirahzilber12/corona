
def max_heapify(A,d, i):
    left = d * i + 1
    right = left + d - 1
    largest = i
    for step in range(left, right+1):
        if step < len(A) and A[step] > A[largest]:
            largest = step
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, d, largest)


def build_max_heap(A, d):
    for i in range(len(A) // d, -1, -1):
        max_heapify(A, d, i)


def heap_extract_max(A, d):
    max = A[0]
    A[0] = A[len(A)-1]
    max_heapify(A, d, 0)
    return max


def insert_key(A, key, d):
    A.append(None)
    return increase_key(A, len(A)-1, key, d)


def increase_key(A, i, key, d):
    A[i] = key
    while i > 0 and A[(i-1)//d] < A[i]:
        A[i], A[(i-1)//d] = A[(i-1)//d], A[i]
        i = (i-1) // d
    return A


def change_increase_key(A, i, key, d):
    if key < A[i]:
        raise ValueError("new key is smaller than current key")
    A[i] = key
    while i > 0 and A[(i-1)//d] < A[i]:
        A[i], A[(i-1)//d] = A[(i-1)//d], A[i]
        i = (i-1) // d
    return A


def delete_key(A, key, d):
    index = find_key_index(A, key)
    A[index], A[len(A)-1] = A[len(A)-1], A[index]
    A = A[0:-1]
    max_heapify(A, d, index)
    return A


def find_key_index(A, key):
    for i in range(0, len(A)):
        if A[i] == key:
            return i



if __name__ == '__main__':
    heap = input("enter numbers to max heap \n")
    heap = heap.split( )
    for i in range(0,len(heap)):
        heap[i] = int(heap[i] )
    d = input("enter num for d \n")
    d = (int(d))

    build_max_heap(heap,d)
    # print("build max heap d =" ,d ,heap)
    # print("the max is : ",heap_extract_max(heap,d))
    # print("the heap after extract max : ",heap)
    # key = input("enter key insert heap  \n")
    # print("heap after insert key :" ,insert_key(heap,int(key),d))
    # key = input("enter key to delete  \n")
    # print("heap after delete key :" ,delete_key(heap, int(key), d))
    print(change_increase_key(heap,1,1,2))