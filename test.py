# _*_ coding:utf-8
"""
@author: andyz
"""

improt numpy as np

def doubleArray(arr):
    """对数组每个元素进行翻倍"""

    arr = np.array(arr)

    return arr**2

if __name__ == '__main__':
    
    arr = [1, 2, 3, 4]

    print(doubleArray(arr))




