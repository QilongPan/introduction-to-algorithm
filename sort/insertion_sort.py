# -*- coding: utf-8 -*-
# @Date    : 2019-08-14 16:50:25
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

def insertion_sort(arr,descent):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j -1
        if descent:
            while i >= 0 and arr[i] < key:
                arr[i+1] = arr[i]
                i = i - 1
        else:
            while i >= 0 and arr[i] > key:
                arr[i+1] = arr[i]
                i = i - 1
        arr[i+1] = key