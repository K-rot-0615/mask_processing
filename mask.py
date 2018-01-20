# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os


def main():
    # 画像の読み込み
    path = './images/20-Hex_1/'
    save_path = "./masked_images/"

    images = []
    for x in os.listdir(path):
        if os.path.isfile(path + x):
            images.append(path + x)

    print(images)

    # マスク画像の読み込み
    mask = cv2.imread("./mask.png", 0)
    for a in range(len(images)):
        img = cv2.imread(images[a])
        print(img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_masked = cv2.bitwise_and(img_gray, img_gray, mask=mask)

        # 表示
        #cv2.imshow("Show MASK Image", img_masked)
        cv2.imwrite(save_path + str(a) + ".png", img_masked)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
