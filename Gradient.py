import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#import random
rate=0.01#learing rate
#线性回归斜率的梯度计算
def da(y,y_p,x):
    return (y-y_p)*(-x)
#线性回归截距的计算
def db(y,y_p):
    return (y-y_p)*(-1)
#根据给定的斜率和截距所有的损失计算
def calc_loss(a,b,x,y):
    temp=y-(a*x+b);
    temp=temp*2
    SSE=sum(temp)/(2*len(x))
    return SSE
def draw_hill(x,y):
    a=np.linspace(-20,20,100)
    print(a)
    b=np.linspace(-20,20,100)
    x=np.array(x)
    y=np.array(y)
    allSSE=np.zeros(shape=(len(a),len(b)))
    for ai in range(0,len(a)):
        for bi in range(0,len(b)):
            a0=a[ai]
            b0=b[bi]
            SSE=calc_loss(a=a0,b=b0,x=x,y=y)
            allSSE[ai][bi]=SSE
    a,b=np.meshgrid(a,b)
    return [a,b,allSSE]
"""
def shuffle_data(x,y):
    #随机打乱x,y的数据，并且保持x和y一一对应
    seed=random.random()
    random.seed(seed)
    random.shuffle(x)
    random.shuffle(y)
"""
x=[30,35,37,59,70,76,88,100]
y=[1100,1423,1377,1800,2304,2588,3495,4839]
#数据归一化
x_max=max(x)
x_min=min(x)
y_max=max(y)
y_min=min(y)
for i in range(0,len(x)):
    x[i]=(x[i]-x_min)/(x_max-x_min)
    y[i]=(y[i]-y_min)/(y_max-y_min)
[ha,hb,hallSSE]=draw_hill(x,y)
hallSSE=hallSSE.T#重要，将所有的losses做一个转置
a=10.0
b=-20.0
fig=plt.figure(1,figsize=(12,8))
fig.suptitle('learning rate:%.2f method:Nestreov momentum'%(rate),fontsize=15)
#绘制图1的曲面
ax=fig.add_subplot(2,2,1,projection='3d')
ax.set_top_view()
ax.plot_surface(ha,hb,hallSSE,rstride=2,cstride=2,cmap='rainbow')
#绘制图2的等高线图
plt.subplot(2,2,2)
ta=np.linspace(-20,20,100)
tb=np.linspace(-10,20,100)
plt.contour(ha,hb,hallSSE,alpha=0.5,cmpa=plt.cm.hot)
C=plt.contour(ha,hb,hallSSE,15,colors='black')
plt.xlabel('a')
plt.ylabel('b')
plt.ion()
all_loss=[]
all_step=[]
last_a=a
last_b=b
va=0
vb=0
gamma=0.9
for step in  range(1,100):
    loss=0
    all_da=0
    all_db=0
    a_ahead=a-gamma*va
    b_ahead=b-gamma*vb
    #shuffle_data(x,y)
    for i in range(0,len(x)):
        y_p=a_ahead*x[i]+b_ahead
        loss=loss+(y[i]-y_p)*(y[i]-y_p)/2
        all_da=all_da+da(y[i],y_p,x[i])
        all_db=all_db+db(y[i],y_p)
    loss=loss/len(x)
    #绘制图1中的loss点
    ax.scatter(a,b,loss,color='black')
    #绘制图2中的loss点
    plt.subplot(2,2,2)
    plt.scatter(a,b,s=5,color='blue')
    plt.plot([last_a,a],[last_b,b],color='aqua')
    #绘制图3中 的回归直线
    plt.subplot(2,2,3)
    plt.plot(x,y)
    plt.plot(x,y,'o')
    x_=np.linspace(0,1,2)
    y_draw=a*x_+b
    plt.plot(x_,y_draw)
    #绘制图4的losses更新曲线
    all_loss.append(loss)
    all_step.append(step)
    plt.subplot(2,2,4)
    plt.plot(all_step,all_loss,color='orange')
    plt.xlabel("step")
    plt.ylabel("loss")
    last_a=a
    last_b=b
    #参数更新
    va=gamma*va+rate*all_da
    vb=gamma*vb+rate*all_db
    a=a-va
    b=a-vb
    if step%1==0:
        print("step: ", step, " loss: ", loss)
        plt.show()
        plt.pause(0.01)
plt.show()
plt.pause(99999999999)
