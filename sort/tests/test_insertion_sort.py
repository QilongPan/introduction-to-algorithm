
# -*- coding: utf-8 -*-
# @Date    : 2019-08-14 17:08:57
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
from introduction_to_algorithm.sort.insertion_sort import insertion_sort


if __name__ == '__main__':
    arr = [10,5,9,3,7]
    insertion_sort(arr,True)
    print(arr)
