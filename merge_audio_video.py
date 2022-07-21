#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:zhengaihua
@file: renames.py
@time: 2022/7/22 13:00
@refer: https://github.com/kkroening/ffmpeg-python
        https://kkroening.github.io/ffmpeg-python/#
        https://ffmpeg.org/ffmpeg.html#Main-options
        https://www.jianshu.com/p/cf1e61eb6fc8
"""
import os
import json
import subprocess

import ffmpeg


def ffmpeg_merge(video_input, audio_input, output):
    video_stream = ffmpeg.input(video_input).video
    audio_stream = ffmpeg.input(audio_input).audio
    (
        ffmpeg
            .output(video_stream, audio_stream.audio, output, vcodec='copy', acodec='copy')
            .run()
    )


def cmd_merge(video_input, audio_input, output):
    # cmd = 'ffmpeg -i %s -i %s -acodec copy -vcodec copy %s' % (audio_input, video_input, output)
    cmd = 'ffmpeg -i {} -i {} -acodec copy -vcodec copy {}'.format(audio_input, video_input, output)
    ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8",
                         timeout=1)
    if ret.returncode == 0:
        print("success:", ret)
    else:
        print("error:", ret)


if __name__ == '__main__':
    root_path = "/Users/zhengaihua/Study/BilibiliDownload"
    # 读取目录下所有文件/文件夹
    for root, dirs, files in os.walk(root_path, topdown=False):
        # for name in dirs:
        #     print(os.path.join(root, name))
        #     print(root, '--'*20)
        for name in files:
            # print(os.path.join(root, name))
            # print(root, '**' * 20)
            if name == 'audio.m4s':
                print(root, '**' * 20)
                audio_input_path = os.path.join(root, name)
                video_input_path = os.path.join(root, "video.m4s")
                # 读取文件名称
                entry_json_path = os.path.join(os.path.abspath(os.path.dirname(root)), "entry.json")
                with open(entry_json_path, 'r') as f:
                    data = json.load(f)
                    dir_name = data["title"].strip()
                    output_name = data["page_data"]["part"].replace(' ', '_') + '.mp4'
                output_dir_path = os.path.join(root_path, dir_name)
                if not os.path.exists(output_dir_path):
                    os.mkdir(output_dir_path)
                output_file_path = os.path.join(output_dir_path, output_name)
                print('audio', audio_input_path)
                print("video", video_input_path)
                print("output_name", output_name)
                print("output_file_path", output_file_path)
                cmd_merge(video_input_path, audio_input_path, output_file_path)