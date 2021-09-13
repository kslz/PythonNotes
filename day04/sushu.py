num = int(input('请输入一个整数：'))
isSuShu = True
for i in range(2, int(num/2)+1,):
    if num % i == 0:
        isSuShu = False
if isSuShu:
    print("%d是素数" % num)
else:
    print("%d不是素数" % num)
