import time as tm


class Main:
    def __init__(self):
        ...

    def start(self, start_str1, start_str2, sleep_time=0.2):
        print(start_str1, end='')
        tm.sleep(sleep_time)
        print('\r' + start_str2)

    def show_dict(self, dict_: dict):
        for k, v in dict_.items():
            print(k, v, sep=': ')
        print()

    def input(self, input_str='[Uranus] @UR-Calculator  Python3  -/\n$'):
        return input(input_str)

    def default(self, foumula: str):
        try:
            print(round(eval(foumula), 16))
        except (ValueError, SyntaxError):
            print('')

    def tree(self, _1, _2, _q, _s):
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

    def nongdu(self, solute, solution):
        res = 1 / solute * solution * 100
        res = str(res) + '%'
        print(res)

    def chick_rabbit(self, footNum, ck_and_rb, ckFoot):
        rbt = (footNum - ckFoot * ck_and_rb) / 2
        print('兔数:', rbt)

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

    def fang_tiji(self, a, b ,h):
        print(a * b * h)

    def yuanzhu(self, S, h):
        print(S * h)

    def yuanzhui(self, S, h):
        print(S * h / 3)
