
# -*- coding: utf-8 -*-
# @Date    : 2019-08-14 17:08:57
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

# os.path.dirname 获取当前文件或目录的父目录路径
# os.path.realpath(__file__)获取当前文件路径
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))

from introduction_to_algorithm.sort.insertion_sort import insertion_sort
from introduction_to_algorithm.comm.array_util import print_array
from introduction_to_algorithm.sort.merge_sort import merge_sort,merge

if __name__ == '__main__':
    arr = [100,68,79,32,46,0,9,42]
 #   arr = [5,9,10,3,7]
#    merge(arr,0,2,4)
    merge_sort(arr,0,len(arr)-1,True)
    print_array(arr)

