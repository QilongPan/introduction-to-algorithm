
# -*- coding: utf-8 -*-
# @Date    : 2019-08-16 14:35:13
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
from introduction_to_algorithm.divide_and_conquer.maximum_subarray import maximum_subarray

if __name__ == "__main__":
    arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    print(arr)
    print(maximum_subarray(arr,0,len(arr) - 1))