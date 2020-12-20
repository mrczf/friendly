import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Window import *
from fctions import Main


class InitWindow(QMainWindow, Ui_MainWindow):
    pro = Main()
    lt = []
    num = ''

    def __init__(self):
        super(InitWindow, self).__init__()
        self.setupUi(self)
        self.s = self.plainTextEdit
        self.rt.clicked.connect(self.rate)
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

    def enter_num0(self, button):
        lt = ' '.join(self.lt)
        lt += '0'
        self.lt = lt.split(' ')
        self.plainTextEdit.setPlainText(lt)


    def enter_num1(self, button):
        lt = ' '.join(self.lt)
        lt += '1'
        self.lt = lt.split(' ')
        self.plainTextEdit.setPlainText(lt)

    def enter_num2(self, button):
        lt = ' '.join(self.lt)
        lt += '2'
        self.lt = lt.split(' ')
        self.plainTextEdit.setPlainText(lt)

    def enter_num3(self, button):
        lt = ' '.join(self.lt)
        lt += '3'
        self.lt = lt.split(' ')
        self.plainTextEdit.setPlainText(lt)

    def enter_num4(self, button):
        lt = ' '.join(self.lt)
        lt += '4'
        self.lt = lt.split(' ')
        self.plainTextEdit.setPlainText(lt)

    def enter_num5(self, button):
        lt = ' '.join(self.lt)
        lt += '5'
        self.lt = lt.split(' ')
        self.plainTextEdit.setPlainText(lt)

    def enter_num6(self, button):
        lt = ' '.join(self.lt)
        lt += '6'
        self.lt = lt.split(' ')
        self.plainTextEdit.setPlainText(lt)

    def enter_num7(self, button):
        lt = ' '.join(self.lt)
        lt += '7'
        self.lt = lt.split(' ')
        self.plainTextEdit.setPlainText(lt)

    def enter_num8(self, button):
        lt = ' '.join(self.lt)
        lt += '8'
        self.lt = lt.split(' ')
        self.plainTextEdit.setPlainText(lt)

    def enter_num9(self, button):
        lt = ' '.join(self.lt)
        lt += '9'
        self.lt = lt.split(' ')
        self.plainTextEdit.setPlainText(lt)

    def enter(self, button):
        string = self.s.toPlainText()
        lt = string.split(' ')
        pro = self.pro

        if lt[0] == 'tr':
            pro.tree(_q=lt[1], _s=lt[2], _1=float(lt[3]), _2=float(lt[4]))
        elif lt[0] == 'ng':
            pro.nongdu(float(lt[1]), float(lt[2]))
        elif lt[0] == 'ckrb':
            pro.chick_rabbit(int(lt[1]), int(lt[2]), int(lt[3]))
        elif lt[0] == 'avr':
            pro.average(float(lt[1]), *lt[2:])
        elif lt[0] == 'rt':
            pro.rate(float(lt[1]), float(lt[2]))

        ##### 图形 #####
        if lt[0] == 'zhouch':
            if lt[1] == 'fang':
                pro.zc_fang(float(lt[2]), float(lt[3]))
            if lt[1] == 'yuan':
                pro.zc_yuan(float(lt[2]))
        if lt[0] == 'mianji':
            if lt[1] == 'fang':
                pro.mj_fang(float(lt[2]), float(lt[3]))
            if lt[1] == 'sanjiao':
                pro.mj_sanj(float(lt[2]), float(lt[3]))
            if lt[1] == 'tixing':
                pro.mj_tixg(float(lt[2]), float(lt[3]), float(lt[4]))
            if lt[1] == 'yuan':
                pro.mj_yuan(float(lt[2]))
        if lt[0] == 'tiji':
            if lt[1] == 'fang':
                pro.tj_fang(float(lt[2]), float(lt[3]), float(lt[4]))
            if lt[1] == 'yuanzhui':
                pro.tj_yhui(float(lt[2]), float(lt[3]))
            if lt[1] == 'yuanzhu':
                pro.tj_yzhu(float(lt[2]), float(lt[3]))

        pro.default(lt)

    def rate(self, button):
        if len(self.lt) == 0:
            self.lt.insert(0, 'rt ')
        else:
            self.lt = ['rt ']
        self.s.setPlainText(' '.join(self.lt))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InitWindow()
    window.show()
    sys.exit(app.exec_())
