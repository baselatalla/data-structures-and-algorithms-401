from quick_sort import __version__
from quick_sort.Quick_Sort import QuickSort


def test_version():
    assert __version__ == '0.1.0'


def test_QuickSort_1():
    arr = [8,4,23,42,16,15]
    left = 0
    right = len(arr) - 1 
    QuickSort(arr,left,right)

    actual = arr
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_QuickSort_2():
    arr = [20,18,12,8,5,-2]
    left = 0
    right = len(arr) - 1 
    QuickSort(arr,left,right)

    actual = arr
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_QuickSort_3():
    arr = [5,12,7,5,5,7]
    left = 0
    right = len(arr) - 1 
    QuickSort(arr,left,right)

    actual = arr
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_QuickSort_4():
    arr = [2,3,5,7,13,11]
    left = 0
    right = len(arr) - 1 
    QuickSort(arr,left,right)

    actual = arr
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected