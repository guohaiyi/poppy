#!/usr/bin/python3
# coding=utf-8

import os
import subprocess
import time

proDir = os.path.split(os.path.realpath(__file__))[0]
shell_file_path = os.path.join(proDir, "../shellFile/")
source_file_path = os.path.join(proDir, "../source/")


class CallShell:
    def __init__(self):
        self.input_file = os.path.join(source_file_path, "sample.mp4")
        self.ffmpeg_file = os.path.join(shell_file_path, "ffmpeg_stream.sh")
        self.re_orc_file = os.path.join(shell_file_path, "restart_orc.sh")
        self.re_omp_file_different = os.path.join(shell_file_path, "restart_omp_different.sh")
        self.re_omp_file_same = os.path.join(shell_file_path, "restart_omp_same.sh")
        self.start_omp_file = os.path.join(shell_file_path, "start_omp.sh")
        self.stop_omp_file = os.path.join(shell_file_path, "stop_omp.sh")
        self.cre_test_file = os.path.join(shell_file_path, "create_test_file.sh")

    def call_ffmpeg(self, stream_link):
        """Live channel推流
        :param stream_link: 推流地址
        :return:
        """
        # 开始推流
        try:
            process = subprocess.Popen(args=[self.ffmpeg_file, self.input_file, stream_link])
        except Exception as e:
            print("执行ffmpeg_stream.sh脚本遇到错误:%s" % e)

        # 等待30秒,待推流结束
        time.sleep(30)

        # 关闭推流进程程序
        try:
            process.terminate()
            pass
        except Exception as e:
            print("关闭程序错误：%s" % e)

    def call_restart_orc(self):
        # 重启orc
        try:
            process = subprocess.Popen(args=[self.re_orc_file])
        except Exception as e:
            print("执行restart_orc.sh脚本遇到错误:%s" % e)

        # 等待5秒，待orc重启完成
        time.sleep(5)

        # 关闭推流进程程序
        try:
            process.terminate()
            pass
        except Exception as e:
            print("关闭程序错误：%s" % e)

    def call_restart_omp_different(self):
        # 重启omp
        try:
            process = subprocess.Popen(args=[self.re_omp_file_different])
        except Exception as e:
            print("执行restart_omp_different.sh脚本遇到错误:%s" % e)

        # 等待35秒，待omp重启完成
        time.sleep(35)

        # 关闭推流进程程序
        try:
            process.terminate()
            pass
        except Exception as e:
            print("关闭程序错误：%s" % e)

    def call_restart_omp_same(self):
        # 重启omp
        try:
            process = subprocess.Popen(args=[self.re_omp_file_same])
        except Exception as e:
            print("执行restart_omp_same.sh脚本遇到错误:%s" % e)

        # 等待35秒，待omp重启完成
        time.sleep(35)

        # 关闭推流进程程序
        try:
            process.terminate()
            pass
        except Exception as e:
            print("关闭程序错误：%s" % e)

    def call_start_omp(self):
        # 启动omp
        try:
            process = subprocess.Popen(args=[self.start_omp_file])
        except Exception as e:
            print("执行start_omp.sh脚本遇到错误:%s" % e)

        # 等待35秒，待omp完成启动
        time.sleep(35)

        # 关闭推流进程程序
        try:
            process.terminate()
            pass
        except Exception as e:
            print("关闭程序错误：%s" % e)

    def call_stop_omp(self):
        # 停止omp
        try:
            process = subprocess.Popen(args=[self.stop_omp_file])
        except Exception as e:
            print("执行stop_omp.sh脚本遇到错误:%s" % e)

        # 等待5秒，待omp停止
        time.sleep(5)

        # 关闭推流进程程序
        try:
            process.terminate()
            pass
        except Exception as e:
            print("关闭程序错误：%s" % e)

    def call_create_test_file(self):
        # 创建测试文件
        try:
            process = subprocess.Popen(args=[self.cre_test_file])
        except Exception as e:
            print("执行create_test_file.sh脚本遇到错误:%s" % e)

        # 等待5秒
        time.sleep(5)

        # 关闭推流进程程序
        try:
            process.terminate()
            pass
        except Exception as e:
            print("关闭程序错误：%s" % e)


if __name__ == '__main__':
    # stream_link = "rtmp://172.16.1.201:44437/live/5d2ff9eaf1854cafc51f79b6"
    call = CallShell()
    call.call_create_test_file()
    # call.call_ffmpeg(stream_link)
