import matplotlib.pyplot as plt
x=[18.6,15.2,13.2,10.6,8.4,33.9]
x1=[18.6,15.2,13.2,10.6,8.4,33.9]
y=['Germany','France','Italy','Spain','Poland','Rest of the EU']



plt.pie(x,labels=y,autopct="%0.1f%%",radius=1.5,
        textprops={"fontsize":10})
plt.pie([1],colors='w',labeldistance=1)

plt.show()