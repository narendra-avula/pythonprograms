__author__ = 'Naidu'
'''
2.Given an array of ints length 6, return an array with the elements "rotated right" by given count.
   arr=[1,2,3,4,5,6]
   rotate_right([1,2,3,4,5,6],2) ? [5,6,1,2,3,4]
   rotate_right([1,2,3,4,5,6],4) ? [3,4,5,6,1,2]

def rotate_right(arr,len):
    pass

'''

def rotate_right(arr, length):
    print arr[len(arr)-length:] + arr[:len(arr)-length]

arr = map(int, raw_input('Enter Numbers\n').split())
length = int(raw_input('Enter Length\n'))
rotate_right(arr, length)