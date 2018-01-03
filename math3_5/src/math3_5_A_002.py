'''
Created on 2018/01/03
aa
@author: EliteBook 8560
'''
# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt


def main():
    x = np.linspace(-3,3,100) # 0～3まで20刻みでxの値を生成
    y =[]
    p=0
    q=0

    for i in x:
        p = 5-(5/9*i**2)
        p1 = math.sqrt(p)
        p2 = math.sqrt(p)*(-1)
        y.append([p1,p2])
        print(p2)

    plt.plot(x,y)      # 曲線を引く
    plt.show()              # グラフ表示

if __name__ == '__main__':
    main()