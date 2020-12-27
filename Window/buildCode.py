l = ['ckrb', 'ng', 'tre', 'rt', 'avr', 'zc fang', 'zc yuan', 'mj fang', 'mj yuan', 'mj sanj', 'mj tixg', 'tj fang',
     'tj yuan', 'tj yzhu', 'tj yhui']
for ll in l:
    print(f'def {ll}(self, button):\n'
          f'    self.lt.insert(0, \'{ll}\' + \' \')\n'
          f'    self.s.setPlainText(\' \'.join(self.lt))\n')