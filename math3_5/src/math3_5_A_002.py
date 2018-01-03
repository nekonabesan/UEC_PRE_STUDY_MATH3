'''
Created on 2018/01/03
@author: EliteBook 8560
数学Ⅲ
第5講 2次曲線
設問A(2)
二次曲線(楕円)
'''
# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt


def main():
    x = np.linspace(-3,3,100) # 0～3まで100刻みでxの値を生成
    y =[]                     # y軸の値を格納する空配列を定義
    p=0
    q=0

    # -3～3の範囲で+-の値を生成し配列へ格納する処理
    for i in x:
        p = 5-(5/9*i**2)
        p1 = math.sqrt(p)
        p2 = math.sqrt(p)*(-1)
        y.append([p1,p2])
        print(p2)

    # 曲線を描画する処理
    plt.plot(x,y)
    # グラフ表示する処理
    plt.show()

if __name__ == '__main__':
    main()