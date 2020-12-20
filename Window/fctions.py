import time as tm
import os
from cover_type import *


class Main:
    def __init__(self):
        ...

    ##### 默认运算 #####
    def default(self, foumula):
        try:
            return round(eval(foumula), 16)
        except (ValueError, SyntaxError, NameError):
            return ''

    ##### 植树问题 #####
    def tree(self, _1, _2, _q, _s):
        # 棵数/全长/株距
        if _q == 'zhuju':
            if _s in ('one', 'rect'):
                return _1 / _2
            elif _s == 'two':
                return _1 / (_2 - 1)
            else:
                return _1 / (_2 + 1)
        if _q == 'keshu':
            if _s in ('one', 'rect'):
                return _1 / _2
            elif _s == 'two':
                return _1 / _2 + 1
            else:
                return _1 / _2 - 1
        if _q == 'quanchang':
            if _s in ('one', 'rect'):
                return _1 * _2
            elif _s == 'two':
                return _1 * (_2 - 1)
            else:
                return _1 * (_2 + 1)

    ##### 计算浓度 #####
    def nongdu(self, solute, solution):
        res = 1 / solute * solution * 100  # 浓度 = 溶质/溶液 * 100%（如：%100 = 10/10 * 100%） “/”指“分之”
        res = str(res) + '%'
        print(res)

    ##### 鸡兔同笼问题 #####
    def chick_rabbit(self, footNum, ck_and_rb, ckFoot):
        rbt = (footNum - ckFoot * ck_and_rb) / 2
        print('兔数:', rbt)

    ##### 平均数 #####
    def average(self, num, *xng):
        n = 0
        for x in (float(i) for i in xng):
            n += x
        return n / num

    ##### 优秀率/及格率/...率 #####
    def rate(self, allow_num, all_num):
        n = round(allow_num / all_num * 100, 2)
        n = str(n) + '%'
        print(n)

    ##### 从这里开始，到 End 结束，这些函数的参数的类型皆为 float，都是关于图形的，特此说明 #####

    def mj_fang(self, a, h):
        print(a * h)

    def zc_fang(self, a, b):
        print((a + b) * 2)

    def mj_sanj(self, a, h):
        print(a * h / 2)

    def mj_tixg(self, a, b, h):
        print((a + b) * h / 2)

    def mj_yuan(self, r):
        print(r * 2 * 3.14)

    def zc_yuan(self, r):
        print(3.14 * (r * r))

    def tj_fang(self, a, b, h):
        print(a * b * h)

    def tj_yzhu(self, S, h):
        print(S * h)

    def tj_yhui(self, S, h):
        print(S * h / 3)

    ##### 上文提到的 End，那条注解的适用范围到此结束，特此说明 #####


'''
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
'''