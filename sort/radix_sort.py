
# -*- coding: utf-8 -*-
# @Date    : 2019-09-19 17:25:22
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

'''
从低位到高位对数的每列排序
'''
def radix_sort(arr,radix=10):
    max_num = max(arr)
    for i in range(len(str(max_num))):
    	bucket = [[] for i in range(radix)]
    	print(arr)
    	for value in arr:
    		print(value)
    		print(value%(radix ** (i+1))//(radix**i))
    		bucket[value%(radix ** (i+1))//(radix**i)].append(value)
    	print(bucket)
    	del arr[:]
    	for buc in bucket:
    		arr.extend(buc)
    print(arr)
    	

arr = [30,45,22,72,9,12,26,80,22,43,1]
radix_sort(arr)
print(arr)