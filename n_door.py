#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:18:16 2022

@author: sun.xijun

Usage: ./n_door.py -h
"""
# import pdb
import h5py
import random
import argparse
from tqdm import tqdm
# pdb.set_trace()


class Ndoor:

    def __init__(self, circle, n, save_file_path):
        """构造函数"""
        self.circle = circle
        self.n = n
        self.save_file_path = save_file_path

    # @staticmethod
    def n_door(self):
        '''
        Parameters
        ----------
        circle : int
            循环测试，要做的实验次数
        n : int
            门的数量
        save_file_path: str
            hd5 保存
        Returns
        -------
        None.

        '''
        origin_door_win = 0
        change_door_win = 0
        # 添加进度条
        for i in tqdm(range(self.circle)):
            # 生成随机的门牌顺序，用于后续删除门的使用
            randam_door_list = random.sample(range(1, self.n+1), self.n)
            choose_door = random.randint(1, self.n)
            treasure_door = random.randint(1, self.n)
            # 打开一扇没有任何标记的门，list中删一个，并随机更换一个门
            for open_door in randam_door_list:
                if open_door != choose_door and open_door != treasure_door:
                    # 排除打开的门
                    randam_door_list.remove(open_door)
                    # 排除选择的门
                    randam_door_list.remove(choose_door)
                    # 换门
                    change_door = randam_door_list[0]
                    break
            # 如果不换门的情况，中奖
            if choose_door == treasure_door:
                origin_door_win += 1
            # 如果换门的情况，中奖
            if change_door == treasure_door:
                change_door_win += 1
        origin_door_win_percent = round((origin_door_win / int(self.circle) * 100), 1)
        change_door_win_percent = round((change_door_win / int(self.circle) * 100), 1)
        print(f"doors: {self.n}\ttrials: {self.circle}", flush=True)
        print(f"origin_door_win: {origin_door_win_percent}%", flush=True)
        print(f"change_door_win: {change_door_win_percent}%", flush=True)
        # 写入hd5文件中
        with h5py.File(self.save_file_path, 'w') as f_out:
            f_out['n_door'] = [self.n, self.circle, origin_door_win_percent, change_door_win_percent]


def parse_arguments():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-n', dest='n', required=False, default=3, type=int,
                        help='the number of doors  (default=3)')
    parser.add_argument('-t', dest='trials', required=False, default=10000, type=int,
                        help='the number of trials (default=10000)')
    parser.add_argument('-s', dest='save_file_path', required=False, default='./n_door.hdf5', type=str,
                        help='the path of save file (default=./n_door.hdf5)')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    circle = args.trials
    n = args.n
    save_file_path = args.save_file_path

    n_door = Ndoor(circle, n, save_file_path)
    n_door.n_door()
