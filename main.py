from fctions import Main

pro = Main()
inputs = 1
helps = {'tr 植树问题': 'tr 要求的东西 (棵数/全长/株距) 植树的形式(one（一端种）two（两端种） zero（两端都不种）rect(封闭图形))  除了A之外其他的数据[此处有2个参数]',
         'ng 浓度': 'ng 溶液重量 溶质重量',
         'ckrb 鸡兔同笼': 'ckrb 总脚数 一只鸡的脚数 总头数',
         'avr 机率': 'avr 符合标准的数量 总数量'}

pro.init('Uranus天王星计算器正在启动中...', 'Fy. [ 版本： 2.3.2 build 202.12.0012 ]\n')
while inputs:
    inputs = pro.input()
    isp = inputs.split(' ')
    if inputs in helps.keys():
        print(inputs, ':', helps[inputs])
    elif inputs == 'help':
        pro.helps(helps)

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
