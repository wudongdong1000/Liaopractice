#小明身高1.75，体重80.5kg。根据BMI公式计算小明的BMI指数
print('这是一个计算BMI指数的程序')
height = float(input('请输入你的身高(米):'))
weight = float(input('请输入你的体重(kg):'))
BMI = weight/(height**2)
str = ['过轻','正常','过重','肥胖','严重肥胖']
if BMI<18.5:
    show = str[0]
elif BMI>=18.5 and BMI<25:
    show = str[1]
elif BMI>=25 and BMI<28:
    show = str[2]
elif BMI>=28 and BMI<32:
    show = str[3]
else:
    show = str[4]
print('您的BMI指数为:%.2f' % BMI,'\n您的身体:',show)