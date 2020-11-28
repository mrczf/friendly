from fctions import Main

pro = Main()
inputs = 1
choices_dict = {'tr': '''
tr A B C D
A: 要求的东西（棵数/全长/株距）
B: 植树的形式（one（一端种）two（两端种） zero（两端都不种）rect（封闭图形））
C、D: 除了A之外其他的数据
''', 'ng': '''
ng A B
A: 溶液重量
B: 溶质重量
''', 'cr': '''
cr A B C
A: 总脚数
B: 一只鸡的脚数
C: 总头数
'''}

pro.start('Uranus天王星计算器正在启动中...', 'Ur. Calculation [版本 1.5]\n*此项目被存放在 Github/Gitee(search: uranus) 上，开源\n\n' + ' '* 20)
while inputs:
    inputs = pro.input()
    isp = inputs.split()
    if inputs in choices_dict.keys():
        print(inputs, ':', choices_dict[inputs])
        continue

    if inputs[0] == "'":
        pro.default(inputs[1:])
        continue
    if isp[0] == 'tree':
        pro.tree(_q=isp[1], _s=isp[2], _1=float(isp[3]), _2=float(isp[4]))
        continue
    if isp[0] == 'ng':
        pro.nongdu(float(isp[1]), float(isp[2]))
        continue
    if isp[0] == 'ckrb':
        pro.chick_rabbit(float(isp[1]), float(isp[2]), float(isp[3]))
        continue
    if isp[0] == 'zhouch':
        if isp[1] == 'fang':
            pro.fang_zhouch(float(isp[2]), float(isp[3]))
        if isp[1] == 'yuan':
            pro.yuan_zhouch(float(isp[2]))
        continue
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
