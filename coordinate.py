from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import warnings;warnings.filterwarnings('ignore')

import os

def detect_contour(dir):
    # 画像を開く
    im = Image.open(dir)
    # リスト化
    im_list = np.asarray(im)
    # im_listの表示
    plt.imshow(im_list)
    # クリック可能回数
    nn = 5
    a = plt.ginput(n=nn)
    # 結果を格納するリスト
    result_list = list()
    for x,y in a:
        # プロット(グラフ)の表示
        plt.plot(x, y, 'ro' )
        # 座標(x, y)をリストに格納
        result_list.append(x)
        result_list.append(y)

    # plt.savefig('fig_test.png', bbox_inches="tight", pad_inches=0.5)
    plt.show()

    return result_list

if __name__ == "__main__":
    print("--------- 処理開始 --------- ")
    # 読み取る画像の取得
    dir = os.path.dirname(os.path.abspath("__file__")) + "読み取る画像のパスを指定"

    result_list = detect_contour(dir)
    # 結果の出力
    print(result_list)
    print("--------- 処理終了 --------- ")
