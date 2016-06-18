__author__ = 'Naidu'
'''
3.Given an array of ints, return array of max 3 elements in the array.
(dont use sort builtin function)
  arr=[8,0,5,15,2,13,7,10]
    output:
    max array=[15,13,10]

def max_3(arr):
    pass

'''

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1] ,alist[i]


def max_3(arr):
    bubbleSort(arr)
    max_array = []
    for num in arr[-3:]:
        max_array.append(num)
    max_array.reverse()
    print max_array


arr=[8,0,5,15,2,13,7,10]
# arr = map(int, raw_input('Enter Numbers\n').split())
max_3(arr)