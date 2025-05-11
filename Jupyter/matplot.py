# %%
import matplotlib

# %%
import matplotlib.pyplot as plt

# %%
plt.plot([1,2,3,4])

# %%
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()

# %%
font1 = {'family':'fantasy', 'color' : 'deeppink', 'weight' : 'normal', 'size' : 'xx-large'}

plt.plot([1,2,3,4] , [1,4,9,16])
plt.xlabel('x', labelpad=30, loc='right', fontdict=font1)
plt.ylabel('yyyy', loc= 'bottom')
plt.show()

# %%
line1 = plt.plot([1,2,3], label='lable1')
line2 = plt.plot([2,4,6], label='lable2')
line3 = plt.plot([3,6,9], label='lable3')
# plt.legend(handles={line1,line2}, loc=(1,0)) # handles 사용시 , 필요
plt.legend()
plt.show()

# %%
line1 = plt.plot([1,2,3], label='lable1')
line2 = plt.plot([2,4,6], label='lable2')
line3 = plt.plot([3,6,9], label='lable3')
plt.legend(ncol=3, fontsize=12, frameon=False, shadow=True)
plt.title('Title Test')
plt.grid(True, axis='both')
plt.show()

# %%
import numpy as np

x = np.arange(3)
y = [100,400,900]

plt.bar(x, y, color=['r','g','b'], width=0.7)
plt.plot(x,y)

plt.xticks(x, ['2018','2019','2020'])
plt.show()

# %%
y = np.arange(3)
x = [100,400,900]

plt.barh(y, x, color=['r','g','b'], height=0.7)
plt.plot(x,y)

plt.yticks(y, ['2018','2019','2020'])
plt.show()

# %%
n = 50
x = np.random.rand(n)
y = np.random.rand(n)

area = (30*np.random.rand(n))**2
colors = np.random.rand(n)

plt.scatter(x,y, s=area, c=colors, cmap='Spectral', alpha=0.5)
plt.show()

# %%
x = [0,1,2]
y = [0,1,2]

area = [1000,2000,3000]

plt.scatter(x,y,area,alpha=0.5)

# %%
radio = [24,28,12,36]
labels = ['A', 'B', 'C', 'D']
wedgeprops = {'width':0.7, 'edgecolor':'k', 'linewidth':1}

plt.pie(radio, labels=labels, autopct='%.1f%%', explode=[0, 0.1, 0, 0.1], colors=['red','yellow','green','purple'],wedgeprops=wedgeprops)
plt.show()

# %%
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2019 = [100,120,140,110,130,150,160,170,180,200,190,210]
sales_2020 = [90,110,130,120,140,160,170,160,150,180,200,190]

line1 = plt.plot(months,sales_2019, label='2019')
line2 = plt.plot(months, sales_2020, label='2020')

plt.xlabel('Month', loc='center')
plt.ylabel('Sales', loc='center')

plt.title('Monthly Sales Comparison (2019-2020)')

plt.legend()
plt.show()

# %%
categories = ['Category 1','Category 2','Category 3','Category 4','Category 5']
data = [20, 35, 15, 27, 45]

plt.bar(categories,data)

plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.grid(True, axis='both')
plt.ylim(0,50)
plt.xticks(rotation=40)

plt.show()

# %%
labels = ['Apple', 'Banana', 'Mango', 'Blueberry']
sizes = [15, 30, 45, 10]
explode = (0,0.1,0,0)

plt.pie(sizes, labels=labels, autopct='%.1f%%', explode=explode, colors=['blue','orange','green','red'], 
        shadow=True, startangle=90)
plt.show()

# %%
x = np.linspace(0, 10, 100)

# sin과 cos 함수의 값을 계산
y_sin = np.sin(x)
y_cos = np.cos(x)

line1 = plt.plot(x, y_sin, 'b', label='sin(x)')
line2 = plt.plot(x, y_cos, 'r', label='cos(x)')

plt.title('Sine and Cosine Functions')
plt.xlabel('X')
plt.ylabel('Y')

plt.grid('both')
plt.legend()

plt.show()


