# How to make  Basic bar plot
import matplotlib.pyplot as plt
x=["Python","C","C++","Java"]
y=[85,70,60,82]
plt.xlabel("Language", fontsize=20)       #xlabel.......
plt.ylabel("Numbers",fontsize=20)          #ylabel.....
plt.title("Popularity Bar" ,fontsize=20)    #bar title.........
c=("y","b","g","m")                         #bar color
plt.bar(x,y,width=0.5,color=c,label="Popularity")
plt.legend()
plt.show()
