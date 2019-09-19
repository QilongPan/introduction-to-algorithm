
# -*- coding: utf-8 -*-
# @Date    : 2019-09-19 17:46:38
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

def bucketSort(arr):
    maximum, minimum = max(arr), min(arr)
    bucketArr = [[] for i in range(maximum // 10 - minimum // 10 + 1)]  
    for i in arr:
        index = i // 10 - minimum // 10
        bucketArr[index].append(i)
    arr.clear()
    for i in bucketArr:
        insertion_sort(i,False)
        arr.extend(i)

if __name__ == '__main__':
    arr = [30,45,22,72,9,12,26,80,22,43,1]
    bucketSort(arr)
    print(arr)