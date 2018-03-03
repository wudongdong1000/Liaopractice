#根据父母身高由遗传公式推算出自子女的身高

Fa_height = int(input('Please input your father\'s height (cm)\n'))
Ma_height = int(input('how about your mother\'s\n'))
boy = (Fa_height+Ma_height)/2*1.08
girl = (Fa_height*0.923+Ma_height)/2
print('boy will be %d\ngirl will be %d' % (boy,girl))
