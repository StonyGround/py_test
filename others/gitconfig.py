"""
批量执行git
"""
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 下午12:50
# @Site    :
# @File    : main.py
# @Software: PyCharm Community Edition
import os


def main():
    # 获取当前目录
    aosp_dir = os.getcwd()
    if not os.path.exists(aosp_dir):
        print('error: %s not exist' % aosp_dir)
        return
    if os.path.isfile(aosp_dir):
        print('error: %s is not dir' % aosp_dir)
        return

    # 遍历文件夹DIR
    for root, dirs, files in os.walk(aosp_dir):
        for _dir in dirs:
            if str(_dir).endswith('.git'):
                path = get_path(root, _dir)
                push_repo(path)


def get_path(_dir, git):
    return _dir + '/' + git


def push_repo(path):
    try:
        os.chdir(path)
        push_cmd = 'git config core.filemode false'
        print(path)
        os.system(push_cmd)

    except Exception as e:
        print('错误 ：', e)


if __name__ == '__main__':
    main()
