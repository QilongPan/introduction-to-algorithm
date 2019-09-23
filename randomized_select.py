
# -*- coding: utf-8 -*-
# @Date    : 2019-09-23 13:59:49
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import random

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

def randomized_select(arr,p,r,i):
    if p == r:
        return arr[p]
    q = random_partition(arr,p,r)
    k = q-p+1
    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr,p,q-1,i)
    else:
        return randomized_select(arr,q+1,r,i-k)

arr = [30,45,22,72,9,12,26,80,22,43,1]
print(randomized_select(arr,0,len(arr)-1,3))