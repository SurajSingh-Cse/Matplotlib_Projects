import matplotlib.pyplot as plt
x= [20,40,60,80,100,120]
y=[120,100,80,60,40,20]

colors=[10,49,30,29,56,40]
sizes=[400,200,400,300,250,350]


plt.xlabel("Depth of Scuba Diver(Ft)",fontsize=20)
plt.ylabel("Water Temperature(*F)", fontsize=20)
plt.title("Scuba Diver Depth vs Water Temperature", fontsize=16)

plt.scatter(x,y,marker="*",c=colors,s=sizes,cmap="viridis")
plt.show()