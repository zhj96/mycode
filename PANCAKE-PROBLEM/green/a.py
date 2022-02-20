
from PIL import ImageGrab
import time


username = "xxxx@qq.com"#发送邮箱
password = "xxxx"
#设定发送的账户，方式
#循环，也可以用while True来代替。
for i in range(1):
    time.sleep(5)#根据需求设定时间
    im = ImageGrab.grab()  # 无参数默认全屏截屏
    im.save('shot.jpg')  # 截图保存，默认是当前目录
    address = "xxxxx@qq.com"#发送到xxx邮箱
    # 标题