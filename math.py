import csv
import math
import matplotlib.pyplot as plt

a=[]
b=[]

x=[]
y=[]
i=0

# 读取csv文件
with open("D:\\作业\\深度学习\\FlightPath.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        #强制类型转换，将需要的值提取出来
        if(float(row[1])!=1):
            #将csv中的数据赋予到列表中
            a.append(float(row[0])*1000)
            b.append(float(row[1])*1000)

#x,y的一些标签定义
plt.xticks(range(0, 25000, 2500))
plt.yticks(range(0, 20000, 2000))
#设置x，y轴的标签
plt.xlabel('X')
plt.ylabel('Y')

#将x轴标签进行一定角度的旋转
plt.xticks(rotation=300)

#绘制雷达的路线图
#figsize : 指定figure的宽和高，单位为英寸，dpi : 指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
plt.figure(figsize=(10, 15), dpi=100)#点图
plt.plot(a, b, c='red')#折线图
plt.scatter(a, b, c='red', s=20, label='无人机路径')

# 读取csv文件
with open("D:\\作业\\深度学习\\LIDARPoints.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(i)
        #强制类型转换，将需要的值提取出来
        if(float(row[1])!=533 and float(row[1])!=534):
            #将极坐标转换为直角坐标
            m=math.cos(float(row[0])/180*math.pi)#坐标转换
            n=math.sin(float(row[0])/180*math.pi)
            x.append(a[i]+float(row[1])*m)
            y.append(b[i]-float(row[1])*n)
            plt.scatter(x, y, c='black', s=10)
        else:
            if(len(x)!=0):
                i += 1
                x.clear()
                y.clear()

# 显示图例，当scatter()函数中有label属性时，必须要有显示图例语句！！即：plt.legend()
plt.legend(loc='best')
# 显示所绘图形
plt.show()



