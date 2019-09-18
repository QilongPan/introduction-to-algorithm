
# -*- coding: utf-8 -*-
# @Date    : 2019-08-16 09:16:20
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

def maximum_subarray(arr,low,high):
    if low == high:
        return low,high,arr[low]
    else:
        mid = (low+high)//2
        left_low,left_high,left_sum = maximum_subarray(arr,low,mid)
        right_low,right_high,right_sum = maximum_subarray(arr,mid+1,high)
        cross_low,cross_high,cross_sum = find_max_crossing_subarray(arr,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low,left_high,left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low,right_high,right_sum
        else:
            return cross_low,cross_high,cross_sum

def find_max_crossing_subarray(arr,low,mid,high):
    arr_sum = 0
    left_sum = None
    max_left = None
    for i in range(mid,low-1,-1):
        arr_sum += arr[i]
        if left_sum == None:
            left_sum = arr_sum
            max_left = i
        else:
            if arr_sum > left_sum:
                left_sum = arr_sum
                max_left = i 
    right_sum = None
    arr_sum = 0
    max_right = None
    for i in range(mid+1,high+1):
        arr_sum += arr[i]
        if right_sum == None:
            right_sum = arr_sum
            max_right = i
        else:
            if arr_sum > right_sum:
                right_sum = arr_sum
                max_right = i
    return max_left,max_right,left_sum+right_sum


