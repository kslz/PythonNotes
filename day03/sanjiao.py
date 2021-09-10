import math

a = float(input('请输入第一个边长'))
b = float(input('请输入第二个边长'))
c = float(input('请输入第三个边长'))
if a + b > c and a + c > b and b + c > a:
    print('周长为： %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积为： %f' % area)
else:
    print('无法构成三角')
