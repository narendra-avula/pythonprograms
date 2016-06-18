__author__ = 'Naidu'
'''
1.Given an array of ints length 6, return an array with the elements "rotated left" by given count.
  example
        arr=[1,2,3,4,5,6]
	rotate_left([1,2,3,4,5,6],2) ? [3,4,5,6,1,2]
	rotate_left([1,2,3,4,5,6],4) ? [5,6,1,2,3,4]

def rotate_left(arr,len):
    pass

'''

def rotate_left(arr, length):
    print arr[length:] + arr[:length]

arr = map(int, raw_input('Enter Numbers\n').split())
length = int(raw_input('Enter Length\n'))
rotate_left(arr, length)