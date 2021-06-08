# Code Challenge-01 Whiteboarding
## Problem Domain:

> > Reverse an array without using any built in function

## In/Out

> > Input: Array of n elements
> > Output: Array in reversed ordered

## Edge cases:

- Empty array
- Null
- Not an array

## Visulization

  - In: [5,3,2,6,4,48,8]
  - Out: [8,48,4,6,2,3,5]


  - In: []

  - Out: []


## Big-O: 

Time Complexity  = O(n) 


## Algortihm:
    1. define new array
    2. loop over the input_array and for every itreation add the last element to the new one and so on until the first elemnt.
    3. return the new array 

## Pseudo Code
    1. Define new array 
    2. index = lengthv-1
    3. for the range of 0- (length of the array)
        1. new_array + arr[length]
        2. length - 1
    4. return new_array 

## Code
```python
  def reverse_array(arr):
      if not( type(arr) == type([]) ):
          return 'error, pleas inter an array !'
      new_array = []
      length = len(arr)
      index = length-1
      for x in range(length):
          new_array += [arr[index]]
          index -= 1
      return print(new_array)

reverse_array([12,3,4])

```


## Verification: 

In: a = [12,3,4]
expected Out: [4,3,12]

length = 3
index = 2
for x in range(3):
x = 0
new_array += [arr[2]]   #([] + [12])
index -1                #( 2 - 1 = 1)
x = 1
new_array += [arr[1]]   #([12] + [3])
index -1                #( 2 - 1 = 1)
x = 2
new_array += [arr[0]]   #([12,3] + [4])
index -1                #( 1 - 1 = 0) 

return [12,3,4]

>>> Verifide
