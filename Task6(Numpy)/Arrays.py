import numpy

def arrays(arr):
    l=numpy.array(arr,float)
    return l[::-1]

arr = input().strip().split(' ')