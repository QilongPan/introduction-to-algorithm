
# -*- coding: utf-8 -*-
# @Date    : 2019-09-19 15:28:45
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import random

def random_quick_sort(arr,p,r):
    if p < r:
        q = random_partition(arr,p,r)
        random_quick_sort(arr,p,q-1)
        random_quick_sort(arr,q+1,r)

def random_partition(arr,p,r):
    index = random.randint(p,r)
    temp = arr[index]
    arr[index] = arr[r] 
    arr[r] = temp
    return partition(arr,p,r)

def partition(arr,p,r):
    x = arr[r]
    i = p 
    for j in range(p,r):
        if arr[j] <= x:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i +1
    temp = arr[i]
    arr[i] = arr[r]
    arr[r] = temp
    return i

if __name__ == '__main__':
    arr = [30,45,22,72,9,12,26,80,22,43,1]
    random_quick_sort(arr,0,len(arr)-1)
    print(arr)