#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:zhengaihua
@E-mail:zhengaihua@jd.com
@file: renames.py
@time: 2021/4/22 13:00
@desc:
"""

import os
import json
import shutil

root = "/Volumes/BilibiliDownload"

if __name__ == '__main__':
    # 读取目录下所有文件/文件夹
    class_list = os.listdir(root)
    print(class_list)
    # 初始化课程文件夹重命名字典 key：老文件名  value：新文件名
    rename_class_dict = dict()
    # 初始化课程文件夹新名字
    class_new_name = None

    # 遍历所有子文件夹
    for class_name in class_list:
        # 课程名称（原始）序号
        print("class_name:", class_name)
        # 课程文件/文件夹路径
        class_path = os.path.join(root, class_name)
        print("class_path:", class_path)
        # 判断文件是否是文件夹
        if os.path.isdir(class_path):
            # 1、获取dvi文件，更新文件夹重命名字典
            dvi_file_name = class_name + '.dvi'
            dvi_file_path = os.path.join(class_path, dvi_file_name)
            print(dvi_file_path)
            if os.path.exists(dvi_file_path):
                with open(dvi_file_path, 'r') as f:
                    title_content = f.read()
                    json_content = json.loads(title_content)
                    class_new_name = json_content["Title"].replace(" ", "_")
                    print("class_new_name:", class_new_name)
                    if class_new_name is not None:
                        rename_class_dict[class_name] = class_new_name
                    class_new_path = os.path.join(root, class_new_name)
            else:
                print("dvi is not exists")
            # 获取每个文件音频
            for part in os.listdir(class_path):
                print("part:", part)
                part_path = os.path.join(class_path, part)
                if os.path.isdir(part_path):
                    # 获取每个文件的文件名
                    info_name = class_name + '.info'
                    info_path = os.path.join(part_path, info_name)
                    if os.path.exists(info_path):
                        with open(info_path, "r") as f:
                            part_content = f.read()
                            part_json = json.loads(part_content)
                            part_name = part_json["PartName"]
                            # part_num = part_json["PartNo"]
                            part_new_name = part_name + '.mp4'

                    for file in os.listdir(part_path):
                        if os.path.splitext(file)[1] == '.mp4':
                            # 重命名视频文件
                            src = os.path.join(part_path, file)
                            dst = os.path.join(part_path, part_new_name)
                            # os.rename(src, dst)
                            shutil.move(src, os.path.join(class_path, part_new_name))
            # 重命名文件夹
            os.rename(class_path, class_new_path)



