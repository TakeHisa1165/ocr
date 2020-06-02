"""
matplotlib で画像を範囲指定し、
拡大表示後に保存
"""


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import crop_by_pil


class CropImage:
    """
    matplotlibで画像を拡大後に保存
    保存は全域を保存し、その後拡大部分を
    別モジュールで切り取り
    """
    def __init__(self, image_path, select_lang, window):
        # 画像を開く
        global DragFlag
        self.select_lang = select_lang
        self.window = window

        self.fnm = image_path
        self.img = Image.open(self.fnm)

        # numpy.ndarrayに
        self.img = np.asarray(self.img)

        # 初期値
        x1 = 0
        y1 = 0
        x2 = 50
        y2 = 50

        # ドラッグしているかのフラグ
        DragFlag = False

        # ソート
        ix1, ix2 = sorted([x1, x2])
        iy1, iy2 = sorted([y1, y2])

        # 画像の一部を抜き出す
        cimg = self.img[iy1:iy2, ix1:ix2, :]

        # plot
        plt.close('all')
        plt.figure(figsize=(10, 8))

        # subplot 1
        plt.subplot(1, 2, 1)
        plt.tight_layout()

        # 画像を描画
        im1 = plt.imshow(self.img, cmap='gray')

        # 四角形を描画
        Rect = [[[x1, x2], [y1, y1]],
                [[x2, x2], [y1, y2]],
                [[x1, x2], [y2, y2]],
                [[x1, x1], [y1, y2]]]

        self.lns = []
        for rect in Rect:
            ln, = plt.plot(rect[0], rect[1], color='r', lw=2)
            self.lns.append(ln)

        # 軸を消す
        plt.axis('off')

        # subplot 2
        plt.subplot(1,2,2)
        self.im2 = plt.imshow(cimg, cmap='gray')
        plt.tight_layout()


        # カラーマップの範囲を合わせる
        plt.clim(im1.get_clim())

        # 軸を消す
        plt.axis('off')

        # イベント
        plt.connect('button_press_event', self.Press)
        plt.connect('motion_notify_event', self.Drag)
        plt.connect('button_release_event', self.Release)

        plt.show()


# 押した時
    def Press(self, event):
        global x1,y1,DragFlag
        # 値がNoneなら終了
        if (event.xdata is None) or (event.ydata is None):
            return

        # 丸める
        cx = int(round(event.xdata))
        cy = int(round(event.ydata))

        x1 = cx
        y1 = cy

        # フラグをたてる
        DragFlag = True

    # ドラッグした時
    def Drag(self, event):
        global x1,y1,x2,y2,DragFlag

        # ドラッグしていなければ終了
        if DragFlag == False:
            return

        # 値がNoneなら終了
        if (event.xdata is None) or (event.ydata is None):
            return

        # 丸める
        cx = int(round(event.xdata))
        cy = int(round(event.ydata))

        x2 = cx
        y2 = cy

        # ソート
        ix1, ix2 = sorted([x1,x2])
        iy1, iy2 = sorted([y1,y2])

        # 画像の一部を抜き出す
        cimg = self.img[iy1:iy2,ix1:ix2,:]

        # 画像を更新
        self.im2.set_data(cimg)

        # 四角形を更新
        self.DrawRect(x1,x2,y1,y2)

        # 描画
        plt.draw()

    # 離した時
    def Release(self, event):
        global DragFlag
        # フラグをたおす
        DragFlag = False
        plt.savefig("cropped_image.png")
        plt.close()
        crop_by_pil.crop_by_pil(select_lang=self.select_lang, window=self.window)

    # 四角形を描く関数
    def DrawRect(self, x1, x2, y1, y2):
        Rect = [[[x1, x2], [y1, y1]],
                [[x2, x2], [y1, y2]],
                [[x1, x2], [y2, y2]],
                [[x1, x1], [y1, y2]]]
        for i, rect in enumerate(Rect):
            self.lns[i].set_data(rect[0], rect[1])

if __name__ == "__main__":
    pass
