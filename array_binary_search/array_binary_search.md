# Code Challenge-03 Whiteboarding

## Problem Domain:

Write a function which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## In/Out

> > Input: Array of n elements , value.
> > Output: index of input value or -1 if its not exesit.

## Edge cases:

- Empty array
- Null
- Not an array

## Visulization

 - In: [4,8,15,16,23,41] ,15
  - Out:2 

  - In: [9,-2,0,4,3] ,4
  - Out: 3   

## Big-O: Look at the code below


## Algortihm:
    1. compares the target value to the middle element of the array.
    2. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half
    3. again taking the middle element to compare to the target value
    4. repeating this until the target value is found
    5. If the search ends with the remaining half being empty, the target is not in the array.


## Pseudo Code
    1. mid = 0 
    1. while 0 <= len(arr) - 1
    2. mid = (high + low) // 2
    3. If x is greater, ignore left half
    4. low = mid + 1
    5. If x is smaller, ignore right half
    6. high = mid - 1
    4. else present in left subarray
    5. means x is present at mid
    6. Then the element was not present
    

## Code

```python
def binary_search(arr, x):
    if not( type(arr) == type([]) ): # If not array
      return 'error' 
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
```


Time Complexity = O(log(n))



## Verification:

```python

Input: a = [2, 5, 7, 8, 9] , x = 8
expected Out: 3

low = 0
high = 5 - 1 = 4
# itration number one
while 0<5 (true) >> 
mid = 0 + 4 = 4 // 2 = 2 so 
if arr[2] < 8 (true) >>
low = 2 + 1 = 3 

# itration number tow
while low =3 <=  high=4  (true) >>
mid =7//2 =3 
if arr[3]<8 (fales) xx
if arr[3]>8 (fales) xx 
return 3   # verified 
 
```