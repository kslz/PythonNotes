from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('1.jpeg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
# im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.convert("1").save('2.jpg', 'jpeg')
# im.save('2.jpg', 'jpeg')
print(im.format, im.size, im.mode)