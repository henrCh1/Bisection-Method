# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:13:07 2023

@author: 86319
"""

def f(x):
    return x**3 - x - 1

def bisection_method(a, b, error):
    # 判断初始区间是否合法
    if f(a) * f(b) >= 0:
        print("Initial interval is invalid.")
        return None
    
    # 初始化迭代次数和根的近似值
    n = 0
    c = (a + b) / 2
    
    # 当根的误差小于指定误差时，退出迭代
    while abs(f(c)) > error:
        # 根据函数值的符号调整区间的左右端点
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        # 更新根的近似值和迭代次数
        c = (a + b) / 2
        n += 1
    
    # 输出结果
    print("Root found at x =", c, "after", n, "iterations.")
    return c

# 在区间[1, 1.5]内求解方程的根
bisection_method(1, 1.5, 0.01)
