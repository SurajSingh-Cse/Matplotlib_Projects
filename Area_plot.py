import matplotlib.pyplot as plt
x=[1,2,3,4,5]
area1=[2,3,2,5,3]
area2=[2,3,4,5,6]
area3=[1,3,2,4,2]


l=["area1","area2","area3"]
plt.stackplot(x,area1,area2,area3,labels=l)
plt.legend(loc=2)
plt.show()