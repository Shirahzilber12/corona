
def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    for i in range(len(A) // 2, 0, -1):
        max_heapify(A, i)


def Heap_Extract_Max(A):
    max = A[0]
    A[0] = A[len(A)-1]
    l = len(A)-1
    max_heapify(A, 0)
    return max


def insert_key(A,key,d):
    A.append(None)
    increase_key(A,len(A)-1,key,d)



def increase_key(A, i, key,d):
    a[i] = key
    while i > 0 and A[((i-1)//d)] < a[i]:
        A[i], A[(i-1)//d] = A[(i-1)//d], A[i]
        i = ((i-1) // d)


# heap =input("e,40,nter numbers to max heap \n")
a = [232,115,8,46,4,5,6,1,3,8,9,11,21,50,60,80,70,61,9,10]

# a = list(a)
build_max_heap(a)
# insert_key(a,1,3)
print(a)
# print(Heap_Extract_Max(a))
# print(a)