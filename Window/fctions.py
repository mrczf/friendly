import time as tm
import os
from cover_type import *


class Main:
    def __init__(self):
        ...

    ### 开始 ###
    def init(self, start_str1, start_str2, sleep_time=0.2):
        start_str1, start_str2 = str_(start_str1, start_str2)
        sleep_time = int(sleep_time)

        os.system('cls')
        print(start_str1, end='')
        tm.sleep(sleep_time)
        print('\r' + start_str2)

    ### 显示帮助 ###
    def helps(self, dict_):
        dict_ = dict(dict_)

        for k, v in dict_.items():
            print(k, v, sep=': ')
        print()

    ### 获取输入 ###
    def input(self, input_str='>'):
        input_str = str(input_str)

        return input(input_str)

    ##### 默认运算 #####
    def default(self, foumula: str):
        try:
            print(round(eval(foumula), 16))
        except (ValueError, SyntaxError, NameError):
            print('')

    ##### 植树问题 #####
    def tree(self, _1: int or float, _2: int or float, _q: str, _s: str):
        # 棵数/全长/株距
        if _q == 'zhuju':
            if _s in ('one', 'rect'):
                print(_1 / _2)
            elif _s == 'two':
                print(_1 / (_2 - 1))
            else:
                print(_1 / (_2 + 1))
            return
        if _q == 'keshu':
            if _s in ('one', 'rect'):
                print(_1 / _2)
            elif _s == 'two':
                print(_1 / _2 + 1)
            else:
                print(_1 / _2 - 1)
            return
        if _q == 'quanchang':
            if _s in ('one', 'rect'):
                print(_1 * _2)
            elif _s == 'two':
                print(_1 * (_2 - 1))
            else:
                print(_1 * (_2 + 1))
            return

    ##### 计算浓度 #####
    def nongdu(self, solute: int or float, solution: int or float):
        res = 1 / solute * solution * 100  # 浓度 = 溶质/溶液 * 100%（如：%100 = 10/10 * 100%） “/”指“分之”
        res = str(res) + '%'
        print(res)

    ##### 鸡兔同笼问题 #####
    def chick_rabbit(self, footNum: int, ck_and_rb: int, ckFoot: int):
        rbt = (footNum - ckFoot * ck_and_rb) / 2
        print('兔数:', rbt)

    ##### 平均数 #####
    def average(self, num, *xiang):
        n = 0
        for x in (float(i) for i in xiang):
            n += x
        print(n / num)

    ##### 优秀率/及格率/...率 #####
    def rate(self, allow_num, all_num):
        n = round(allow_num / all_num * 100, 2)
        n = str(n) + '%'
        print(n)

    ##### 从这里开始，到 End 结束，这些函数的参数的类型皆为 float，都是关于图形的，特此说明 #####

    def fang_mianji(self, a, h):
        print(a * h)

    def fang_zhouch(self, a, b):
        print((a + b) * 2)

    def sanjiao_mianji(self, a, h):
        print(a * h / 2)

    def tixing_mianji(self, a, b, h):
        print((a + b) * h / 2)

    def yuan_mianji(self, r):
        print(r * 2 * 3.14)

    def yuan_zhouch(self, r):
        print(3.14 * (r * r))

    def fang_tiji(self, a, b, h):
        print(a * b * h)

    def yuanzhu(self, S, h):
        print(S * h)

    def yuanzhui(self, S, h):
        print(S * h / 3)

    ##### 上文提到的 End，那条注解的适用范围到此结束，特此说明 #####


def mainLoop(helps):
    pro = Main()
    pro.init('Fy is Starting...', 'Fy. [ 版本： 2.3.2 build 202.12.0012 ]')
    while True:
        inputs = pro.input()
        print(' ', end='')
        isp = inputs.split(' ')
        if inputs in helps.keys():
            print(inputs, ':', helps[inputs])
        elif inputs == 'help':
            pro.helps(helps)
        elif inputs in ('', 'exit', 'quit', 'e', 'q', 'ext', 'qt'):
            break

        if isp[0] == 'tr':
            pro.tree(_q=isp[1], _s=isp[2], _1=float(isp[3]), _2=float(isp[4]))
        elif isp[0] == 'ng':
            pro.nongdu(float(isp[1]), float(isp[2]))
        elif isp[0] == 'ckrb':
            pro.chick_rabbit(int(isp[1]), int(isp[2]), int(isp[3]))
        elif isp[0] == 'avr':
            pro.average(float(isp[1]), *isp[2:])
        elif isp[0] == 'rt':
            pro.rate(float(isp[1]), float(isp[2]))

        ##### 图形 #####
        if isp[0] == 'zhouch':
            if isp[1] == 'fang':
                pro.fang_zhouch(float(isp[2]), float(isp[3]))
            if isp[1] == 'yuan':
                pro.yuan_zhouch(float(isp[2]))
        if isp[0] == 'mianji':
            if isp[1] == 'fang':
                pro.fang_mianji(float(isp[2]), float(isp[3]))
            if isp[1] == 'sanjiao':
                pro.sanjiao_mianji(float(isp[2]), float(isp[3]))
            if isp[1] == 'tixing':
                pro.tixing_mianji(float(isp[2]), float(isp[3]), float(isp[4]))
            if isp[1] == 'yuan':
                pro.yuan_mianji(float(isp[2]))
        if isp[0] == 'tiji':
            if isp[1] == 'fang':
                pro.fang_tiji(float(isp[2]), float(isp[3]), float(isp[4]))
            if isp[1] == 'yuanzhui':
                pro.yuanzhui(float(isp[2]), float(isp[3]))
            if isp[1] == 'yuanzhu':
                pro.yuanzhu(float(isp[2]), float(isp[3]))

        pro.default(inputs)
