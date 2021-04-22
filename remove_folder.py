#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:zhengaihua
@E-mail:zhengaihua@jd.com
@file: remove_folder.py
@time: 2021/4/22 18:05
@desc:
"""

import os
import shutil

root = "/Volumes/Alisa/BilibiliDownload"

if __name__ == '__main__':
    # 读取目录下所有文件/文件夹
    class_list = os.listdir(root)
    print(class_list)
    os.chmod(root, 0o755)
    # 遍历所有子文件夹
    for class_name in class_list:
        # 课程名称（原始）序号
        print("class_name:", class_name)
        # 课程文件/文件夹路径
        class_path = os.path.join(root, class_name)
        # print("class_path:", class_path)
        # 判断文件是否是文件夹
        if os.path.isdir(class_path):
            # 获取每个文件
            for folder in os.listdir(class_path):
                # print("folder:", folder)
                folder_path = os.path.join(class_path, folder)
                if os.path.isdir(folder_path):
                    os.chmod(folder_path, 0o755)
                    print("folder_path:", folder_path)
                    shutil.rmtree(folder_path)

                if os.path.splitext(folder)[1] == '.dvi' or os.path.splitext(folder)[1] == '.ini':
                    os.remove(folder_path)

