import matplotlib.pyplot as plt
x=[10,20,15,30,25]
x1=[30,15,20,10,25]
x2=[25,35,10,14,16]
x3=[25,35,10,14,16]
x4=[25,35,10,14,16]
x5=[100]

y=["A","B","C","D","E"]
y1=["F","G","H","I","J"]
y2=["K","L","M","N","O"]
y3=["P","Q","R","S","T"]
y4=["U","V","W","X","Y"]
y5=["Z"]


plt.pie(x,labels=y,radius=1.2,labeldistance=0.9)
plt.pie(x1,radius=1,labels=y1,labeldistance=0.9)
plt.pie(x2,radius=0.8,labels=y2,labeldistance=0.85)
plt.pie(x3,labels=y3,radius=0.6,labeldistance=0.8)
plt.pie(x4,labels=y4,radius=0.4,labeldistance=0.7)
plt.pie(x5,labels=y5,radius=0.2,labeldistance=0)

plt.show()