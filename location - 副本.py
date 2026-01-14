# 导入需要的库
import seekfree, pyb

import sensor, image, time, math
import os, tf
from pyb import LED
from machine import UART

# 初始化屏幕
lcd = seekfree.LCD180(3)

# 初始化摄像头
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_brightness(1500)
sensor.skip_frames(time = 10)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(True,(0,0,0))
# 初始化串口 波特率设置为115200
uart = UART(2, baudrate=115200)


x_num=[]
y_num=[]
count=0
flag1=0
path=[]
def usart():
    path.append('c')
    for i in range(0,11):
        if int(x_num[i]/10)==0:
            path.append('0')
        path.append(str(x_num[i]))
        if int(y_num[i]/10)==0:
           path.append('0')
        path.append(str(y_num[i]))



    sum="".join(path)
    print(sum)
    #uart.write(sum)
    path.clear()





while(True):
    # 截取当前图像
    img = sensor.snapshot()
    # 在图像中搜索矩形
    for r in img.find_rects(threshold = 2000):
        # 判断矩形是否满足要求
        if r.w() > 120 and r.w() < 180 and r.h() > 70 and r.h() < 130:
            # 绘制矩形外框，便于在IDE上查看识别到的矩形位置
            img.draw_rectangle(r.rect(), color = (255, 0, 0))

            #在矩形中搜索圆形
            for c in img.find_circles(roi = r.rect(), threshold = 1800, x_margin = 5, y_margin = 5, r_margin = 5,r_min = 2, r_max = 4, r_step = 1):
                # 绘制圆形外框
                img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))
                # 计算实际X坐标点
                posx = (float(c.x()) - float(r.x())) / float(r.w()) * 35 + 1
                # 计算实际Y坐标点
                posy = 25 - ((float(c.y()) - float(r.y())) / float(r.h()) * 25) + 1
                # 将坐标点绘制到图像上
                img.draw_string(c.x() - 5, c.y() - 10, "(" + str(int(posx)) + "," + str(int(posy)) + ")", color = (0, 0, 255), scale = 1, mono_space = False)

                if count>=12:
                    usart()

                    #print(x_num)
                    #print(y_num)
                    count=0
                    LED(2).on()


                    x_num.clear()
                    y_num.clear()

                x_num.append(int(posx))
                y_num.append(int(posy))

                for j in range(count):
                    if x_num[j]==x_num[count] and y_num[j]==y_num[count]:
                        del x_num[count]
                        del y_num[count]
                        count-=1
                count+=1




