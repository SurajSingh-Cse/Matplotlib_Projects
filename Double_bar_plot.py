import matplotlib.pyplot as plt
import numpy as np
x=["Python","C","C++","Java","JavaScript"]
y=[85,70,60,82,50]
z=[20,30,40,50,60]

width=0.4
p=np.arange(len(x))
p1=[j+width for j in p]

plt.xlabel("Language", fontsize=20)       #xlabel.......
plt.ylabel("Numbers",fontsize=20)          #ylabel.....
plt.title("Popularity Bar" ,fontsize=20)    #bar title.........

plt.bar(p,y,width,color="m",label="Popularity")
plt.bar(p1,z,width,color="b",label="Popularity")\

plt.xticks(p+width/2,x,rotation=20)
plt.legend()
plt.show()
