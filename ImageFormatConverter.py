"""
# -*- coding: utf-8 -*-
# @Title : ImageFormateConverter.py
# @Time : 2021/10/16 11:25
# @Author : Shengle_Wang
# @Site : https://jfsblog.com
"""

import cv2
import os
import glob

folderPath = input('■資料夾路徑(不可有中文):') + '\\'
originalFormat = str(input('■原檔案格式(大小寫一致): .'))
newFormat = str(input('■欲變更檔案格式: .'))
resize_width = int(input('■欲變更檔案整數寬度(px):'))
filepath = glob.glob(folderPath + '*.' + str(originalFormat))

SLfilelist = []
n = 0
for i in filepath:
    SLfilelist.append(os.path.splitext(os.path.basename(filepath[n]))[0])
    n = n + 1
# print(SLfilelist)

n = 0
for i in SLfilelist:
    oldpath = folderPath + SLfilelist[n] + '.' + str(originalFormat)
    newpath = folderPath + str(n + 1) + '.' + str(originalFormat)
    os.rename(oldpath, newpath)
    img = cv2.imread(newpath)
    print(newpath)
    ratio = img.shape[0] / img.shape[1]
    resize_height = round(resize_width * ratio)
    img_resize = cv2.resize(img, (resize_width, resize_height))
    cv2.imwrite (str(folderPath) + str(newFormat) + '_version_' + str(SLfilelist[n]) + '.' + str(newFormat), img_resize)
    os.rename(newpath, oldpath)
    n = n + 1

print("\n■修正完成！")