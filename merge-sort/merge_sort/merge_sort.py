def Mergesort(arr):
    n = len(arr)
    if n > 1 :
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        
        Mergesort(left)
        Mergesort(right)
        Merge(left,right,arr)
    return arr 

def Merge(left,right,arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and  j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1 
        else:
            arr[k] = right[j]
            j += 1 

        k += 1 

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1



if __name__ == '__main__':
    arr = [2,3,5,7,13,11]
    sorted_array = Mergesort(arr)
    print(sorted_array)