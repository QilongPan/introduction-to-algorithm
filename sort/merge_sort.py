
# -*- coding: utf-8 -*-
# @Date    : 2019-08-15 16:40:11
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

def merge_sort(arr,left,right,descent):
    if left < right:
        middle = (right + left) // 2
        merge_sort(arr,left,middle,descent)
        merge_sort(arr,middle+1,right,descent)
        merge(arr,left,middle,right,descent)

def merge(arr,left,middle,right,descent):
    left_arr_len = middle - left + 1
    right_arr_len = right - middle
    left_arr = []
    right_arr = []
    for i in range(left_arr_len):
        left_arr.append(arr[left+i])
    for i in range(right_arr_len):
        right_arr.append(arr[middle+1+i])
    i = 0
    j = 0
    k = left
    while i < left_arr_len and j < right_arr_len:
        if descent:
            if left_arr[i] >= right_arr[j]:
                arr[k] = left_arr[i]
                i = i + 1
            else:
                arr[k] = right_arr[j]
                j = j + 1               
        else:
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i = i + 1
            else:
                arr[k] = right_arr[j]
                j = j + 1        
        k = k + 1
    while i < left_arr_len:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < right_arr_len:
        arr[k] = right_arr[j]
        j += 1
        k += 1    

