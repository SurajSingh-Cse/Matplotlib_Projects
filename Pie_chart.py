import matplotlib.pyplot as plt
x=[18.6,15.2,13.2,10.6,8.4,33.9]
y=['Germany','France','Italy','Spain','Poland','Rest of the EU']
ex=[0.0,0.0,0.0,0.4,0.0,0.0]


plt.pie(x,labels=y,explode=ex,autopct="%0.1f%%",shadow=True,radius=1.2,startangle=180,
        textprops={"fontsize":10})
plt.title("Population of countries of the European Union in 2021 by percentage")
plt.legend(loc=2)
plt.show()