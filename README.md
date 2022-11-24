# n-door

n-door 选择换不换门的问题

## Getting started
问题描述：
n (i.e. n=3) 扇门中有一扇门后面有财宝，每扇门后面有财宝的概率是多少？ 主持人让你选择一扇但不打开。 接着， 他打开任意一扇没有财 宝的门后问你， 你愿不愿意更换你的第一选择（=选择另一扇门）？
从概率的角度来看：
- 概率1：不换门获得财宝的概率。
- 概率2：选择换门后的获得财宝的概率。

```bash
./n_door.py

usage: n_door.py [-h] [-n N] [-t TRIALS] [-s SAVE_FILE_PATH]

optional arguments:
  -h, --help         show this help message and exit
  -n N               the number of doors (default=3)
  -t TRIALS          the number of trials (default=10000)
  -s SAVE_FILE_PATH  the path of save file (default=./n_door.hdf5)
```
