
# -*- coding: utf-8 -*-
# @Date    : 2019-09-19 16:35:18
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
'''
例如排序数组arr = [2,5,3,0,2,3,0,3]
1.首先统计每个数的数量 arr3的长度k是排序数字的max-min+1 为6 [2,0,2,3,0,1]
如果简单的方式可以直接根据数量表输出排序后数组了，但是需要两层for循环
2.高级一点的做法为：算出每个数的最终位置 [2,2,4,7,7,8]
3，遍历原始数组arr,将选中的数放入其对应的最终位置，并将最终位置往前移动一位

'''
def counting_sort(arr1,arr2,k):
    min_num = min(arr1)
    arr3 = [0 for i in range(k)]
    #1
    for i in range(len(arr1)):
        num = arr1[i] - min_num
        arr3[num] = arr3[num]+1
    print(arr3)
    #2
    for i in range(1,k):
        arr3[i] = arr3[i]+arr3[i-1]
    print(arr3)
    #3
    for i in range(len(arr1)-1,-1,-1):
        arr2[arr3[arr1[i]-min_num]-1] = arr1[i]
        arr3[arr1[i]-min_num] = arr3[arr1[i]-min_num] - 1

arr = [2,5,3,0,2,3,0,3]
sort_arr = [-1 for i in range(len(arr))]
counting_sort(arr,sort_arr,max(arr)-min(arr)+1)
print(sort_arr)
