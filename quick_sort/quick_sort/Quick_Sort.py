def QuickSort(arr,left,right):
    if left < right:
        position = partition(arr,left,right)
        QuickSort(arr,left,position - 1)
        QuickSort(arr,position + 1, right)


def partition(arr,left,right):
    pivot = arr[right]
    low = left - 1

    for i in range(left ,right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i ,low)

    swap(arr ,right , low + 1)
    return (low + 1)

def swap(arr , i , low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp



if __name__ == '__main__':
    arr = [8,4,23,42,16,15]
    left = 0
    right = len(arr) - 1 
    QuickSort(arr,left,right)
    print(arr)