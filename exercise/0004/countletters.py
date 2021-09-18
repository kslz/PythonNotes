"""查询文件中的单词个数"""
import re

txtfile = open("./1.txt")
txt_str=txtfile.read()
txt_new=re.sub(r'\W'," ",txt_str)
count = txt_new.count(" ")+1
print(count)