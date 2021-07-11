# Insertion Sort

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part


## Pseudocode

```py

  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

```


## Trace

`Sample Array: [8,4,23,42,16,15]`

### Pass 1:

[8,4,23,42,16,15]
 0 1  2  3  4  5

j = 0
temp = 4

while 0 >= 0 and 4 < 8:
  arr[1] = 8
  j = -1
while -1 >= 0 and 4 < 8:
>>>>

arr[0] = 4

 ==>[4,8,23,42,16,15]
     0 1 2  3  4  5

* in the first pass we compare the values of the index 0 and 1 where value of index 0 grater than the value of index 1 so we swaped the possitions as the output
  
### Pass 2:

[4,8,23,42,16,15]
 0 1  2  3  4  5

j = 2
temp = 23

while 1 >= 0 and 23 < 8:
  >>>

arr[2] = 23

==> [4,8,23,42,16,15]
     0 1 2  3  4  5

* In the second pass aftre comparing values index 1 and 2 where  value of ind 2 grater than 1 nothing happen the array
  
### Pass 3:

[4,8,23,42,16,15]
 0 1  2  3  4  5

j = 2
temp = 42

while  2 >= 0 and 42 < 23:
  >>>

arr[3] = 42

==> [4,8,23,42,16,15]
     0 1 2  3  4  5

* In the second pass aftre comparing values index 2 and 3 where  value of ind 3 grater than 2 nothing happen the array.


### Pass 4:

[4,8,23,42,16,15]
 0 1  2  3  4  5

j = 3
temp = 16

while  3 >= 0 and 16 < 42:
  arr[4] = 42
  j = 2

while  2 >= 0 and 16 < 23:
  arr[3] = 23
  j = 1
while  1 >= 0 and 16 < 8:
>>>>>

arr[2] = 16

==> [4,8,16,23,42,15]
     0 1 2  3  4  5

* in this pass after comparing values of indexs 3 ,4 where value of 3 grater than of 4 so we swaped the possitions then we compare  values of indexs 2 ,3 where value of 2 grater than value of 3  so we swaped the possitions.


### Pass 5:

[4,8,16,23,42,15]
 0 1  2  3  4  5

j = 4
temp = 15

while  4 >= 0 and 15 < 42:
  arr[5] = 42
  j = 3

while  3 >= 0 and 15 < 23 :
  arr[4] = 23
  j = 2
while  2 >= 0 and 15 < 16 :
  arr[3] = 16
  j = 1
while  1 >= 0 and 15 < 8 :
>>>>>

arr[2] = 15

==> [4,8,15,16,23,42]
     0 1 2  3  4  5

* in this pass after comparing values of indexs 4 ,5 where value of 4 grater than index 5 so we swaped the possitions then we comparing values of indexs 3 ,4 where value of 3 grater than index 4 so we swaped the possitions then we comparing values of indexs 2 ,3 where value of 2 grater than index 3 so we swaped the possitions.
  
