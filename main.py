import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow
from Window import *
from fctions import Main


class InitWindow(QMainWindow, Ui_MainWindow):
    pro = Main()
    lt = []

    def __init__(self):
        super(InitWindow, self).__init__()
        self.setupUi(self)
        self.setIconSize(QSize(74, 74))
        self.setWindowTitle('Friendly')
        self.setWindowIcon(QIcon('./ICO.ico'))
        self.s = self.Command
        self.r = self.ResultNum

        self.rt.clicked.connect(self.rate)
        self.tre.clicked.connect(self.tree)
        self.avr.clicked.connect(self.avrs)
        self.ng.clicked.connect(self.nongdu)
        self.ckrb.clicked.connect(self.cknrbt)
        self.qunch.clicked.connect(self.trqc)
        self.zhuju.clicked.connect(self.trzj)
        self.keshu.clicked.connect(self.trks)
        self.sin.clicked.connect(self.sinn)
        self.cos.clicked.connect(self.coss)
        self.tan.clicked.connect(self.tann)
        self.sqrt.clicked.connect(self.sqrts)
        self.abs.clicked.connect(self.abss)

        self.zc_fang.clicked.connect(self.zcfang)
        self.zc_yuan.clicked.connect(self.zcyuan)
        self.mj_fang.clicked.connect(self.mjfang)
        self.mj_yuan.clicked.connect(self.mjyuan)
        self.mj_tixg.clicked.connect(self.mjtixg)
        self.mj_sanj.clicked.connect(self.mjsanj)
        self.tj_fang.clicked.connect(self.tjfang)
        self.tj_yuan.clicked.connect(self.tjyuan)
        self.tj_yzhu.clicked.connect(self.tjyzhu)
        self.tj_yhui.clicked.connect(self.tjyhui)

        self.key0.clicked.connect(self.enter_num0)
        self.key1.clicked.connect(self.enter_num1)
        self.key2.clicked.connect(self.enter_num2)
        self.key3.clicked.connect(self.enter_num3)
        self.key4.clicked.connect(self.enter_num4)
        self.key5.clicked.connect(self.enter_num5)
        self.key6.clicked.connect(self.enter_num6)
        self.key7.clicked.connect(self.enter_num7)
        self.key8.clicked.connect(self.enter_num8)
        self.key9.clicked.connect(self.enter_num9)
        self.num_dot.clicked.connect(self.dot)
        self.leftq.clicked.connect(self.lfq)
        self.rightq.clicked.connect(self.rtq)

        self.Plus.clicked.connect(self.plus)
        self.Minus.clicked.connect(self.minus)
        self.Times.clicked.connect(self.times)
        self.Division.clicked.connect(self.divs)
        self.Remainder.clicked.connect(self.remainder)
        self.Exact.clicked.connect(self.exact)
        self.Power.clicked.connect(self.power)

        self.Spaces.clicked.connect(self.spaces)
        self.EnterButton.clicked.connect(self.enter)
        self.AC.clicked.connect(self.clear)
        self.BK.clicked.connect(self.back)
    '''
    def psng(self, button):
        lt = [x for i in self.lt for x in re.split(r'\+|-|\*|/|^|%|//', i)]
        if len(self.lt) != 0:
            if abs(float(lt[-1])) == float(lt[-1]):
                self.lt[-1] = '-' + str(lt[-1])
            else:
                self.lt[-1] = (lt[-1])[1:]
        tmp = 0 - len(lt[-1]) -1
        self.lt[tmp:] = lt[-1]
        self.s.setPlainText(' '.join(self.lt))
    '''
    def enter(self, button):
        string = self.s.toPlainText()
        lt = string.split()
        lt = [lt[0]] + [self.pro.default(x) for x in lt[1:]]
        rs = ''
        pro = self.pro
        if string.strip() == '':
            return
        try:
            if string[0] not in [str(i) for i in range(1, 11)]:
                if lt[0] == 'tre':
                    rs = pro.tree(_q=lt[1], _s=lt[2], _1=float(lt[3]), _2=float(lt[4]))
                elif lt[0] == 'ng':
                    rs = pro.nongdu(float(lt[1]), float(lt[2]))
                elif lt[0] == 'ckrb':
                    rs = pro.chick_rabbit(int(lt[1]), int(lt[2]), int(lt[3]))
                elif lt[0] == 'avr':
                    rs = pro.average(float(lt[1]), *lt[2:])
                elif lt[0] == 'rt':
                    rs = pro.rate(float(lt[1]), float(lt[2]))
                elif lt[0] == 'sin':
                    rs = pro.sin(float(lt[1]))
                elif lt[0] == 'cos':
                    rs = pro.cos(float(lt[1]))
                elif lt[0] == 'tan':
                    rs = pro.tan(float(lt[1]))
                elif lt[0] == 'abs':
                    rs = pro.abs(float(lt[1]))
                elif lt[0] == 'sqrt':
                    rs = pro.sqrt(float(lt[1]))

                ##### 图形 #####
                if lt[0] == 'zc':
                    if lt[1] == 'fang':
                        rs = pro.zc_fang(float(lt[2]), float(lt[3]))
                    if lt[1] == 'yuan':
                        rs = pro.zc_yuan(float(lt[2]))
                if lt[0] == 'mj':
                    if lt[1] == 'fang':
                        rs = pro.mj_fang(float(lt[2]), float(lt[3]))
                    if lt[1] == 'sanj':
                        rs = pro.mj_sanj(float(lt[2]), float(lt[3]))
                    if lt[1] == 'tixg':
                        rs = pro.mj_tixg(float(lt[2]), float(lt[3]), float(lt[4]))
                    if lt[1] == 'yuan':
                        rs = pro.mj_yuan(float(lt[2]))
                if lt[0] == 'tj':
                    if lt[1] == 'fang':
                        rs = pro.tj_fang(float(lt[2]), float(lt[3]), float(lt[4]))
                    if lt[1] == 'yhui':
                        rs = pro.tj_yhui(float(lt[2]), float(lt[3]))
                    if lt[1] == 'yzhu':
                        rs = pro.tj_yzhu(float(lt[2]), float(lt[3]))
            elif string.strip() != '' and string != '>>>':
                rs = pro.default(string.replace('^', '**'))
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, '数据错误', str(e))
        else:
            self.r.setPlainText(str(rs))

    def dot(self, button):
        lt = ' '.join(self.lt)
        lt += '.'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def sqrts(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'sqrt' + ' ')
        else:
            self.lt = ['sqrt' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def abss(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'abs' + ' ')
        else:
            self.lt = ['abs' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def sinn(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'sin' + ' ')
        else:
            self.lt = ['sin' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def coss(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'cos' + ' ')
        else:
            self.lt = ['cos' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def tann(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'tan' + ' ')
        else:
            self.lt = ['tan' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def lfq(self, button):
        lt = ' '.join(self.lt)
        lt += '('
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def rtq(self, button):
        lt = ' '.join(self.lt)
        lt += ')'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def remainder(self, button):
        lt = ' '.join(self.lt)
        lt += '%'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def power(self, button):
        lt = ' '.join(self.lt)
        lt += '^'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def exact(self, button):
        lt = ' '.join(self.lt)
        lt += '//'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def plus(self, button):
        lt = ' '.join(self.lt)
        lt += '+'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def minus(self, button):
        lt = ' '.join(self.lt)
        lt += '-'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def times(self, button):
        lt = ' '.join(self.lt)
        lt += '*'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def divs(self, button):
        lt = ' '.join(self.lt)
        lt += '/'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def clear(self, button):
        self.lt = []
        self.s.setPlainText('>')
        self.r.setPlainText('0.')

    def back(self, button):
        if len(self.s.toPlainText()) == 1:
            self.s.setPlainText('>')
            self.lt = ['']
        elif self.s.toPlainText().strip() != '':
            string = self.s.toPlainText()
            string = string[:-1]
            self.lt = string.split(' ')
            self.s.setPlainText(string)

    def trqc(self, button):
        self.lt.insert(1, 'qunch' + ' ')
        self.s.setPlainText(' '.join(self.lt))

    def trzj(self, button):
        self.lt.insert(1, 'zhuju' + ' ')
        self.s.setPlainText(' '.join(self.lt))

    def trks(self, button):
        self.lt.insert(1, 'keshu' + ' ')
        self.s.setPlainText(' '.join(self.lt))

    def enter_num0(self, button):
        lt = ' '.join(self.lt)
        lt += '0'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def enter_num1(self, button):
        lt = ' '.join(self.lt)
        lt += '1'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def enter_num2(self, button):
        lt = ' '.join(self.lt)
        lt += '2'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def enter_num3(self, button):
        lt = ' '.join(self.lt)
        lt += '3'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def enter_num4(self, button):
        lt = ' '.join(self.lt)
        lt += '4'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def enter_num5(self, button):
        lt = ' '.join(self.lt)
        lt += '5'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def enter_num6(self, button):
        lt = ' '.join(self.lt)
        lt += '6'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def enter_num7(self, button):
        lt = ' '.join(self.lt)
        lt += '7'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def enter_num8(self, button):
        lt = ' '.join(self.lt)
        lt += '8'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def enter_num9(self, button):
        lt = ' '.join(self.lt)
        lt += '9'
        self.lt = lt.split(' ')
        self.s.setPlainText(lt)

    def spaces(self, button):
        self.lt.append('')

    def cknrbt(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'ckrb' + ' ')
        else:
            self.lt = ['ckrb' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def nongdu(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'ng' + ' ')
        else:
            self.lt = ['ng' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def tree(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(10)]:
            self.lt.insert(0, 'tr' + ' ')
        else:
            self.lt = ['tr' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def rate(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'rt' + ' ')
        else:
            self.lt = ['rt' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def avrs(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'avr' + ' ')
        else:
            self.lt = ['avr' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def zcfang(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'zc fang' + ' ')
        else:
            self.lt = ['zc fang' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def zcyuan(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'zc yuan' + ' ')
        else:
            self.lt = ['zc yuan' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def mjfang(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'mj fang' + ' ')
        else:
            self.lt = ['mj fang' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def mjyuan(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'mj yuan' + ' ')
        else:
            self.lt = ['mj yuan' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def mjsanj(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'mj sanj' + ' ')
        else:
            self.lt = ['mj sanj' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def mjtixg(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'mj tixg' + ' ')
        else:
            self.lt = ['mj tixg' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def tjfang(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'tj fang' + ' ')
        else:
            self.lt = ['tj fang' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def tjyuan(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'tj yuan' + ' ')
        else:
            self.lt = ['tj yuan' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def tjyzhu(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'tj yzhu' + ' ')
        else:
            self.lt = ['tj yzhu' + ' ']
        self.s.setPlainText(' '.join(self.lt))

    def tjyhui(self, button):
        if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)]:
            self.lt.insert(0, 'tj yhui' + ' ')
        else:
            self.lt = ['tj yhui' + ' ']
        self.s.setPlainText(' '.join(self.lt))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InitWindow()
    window.show()
    sys.exit(app.exec_())
