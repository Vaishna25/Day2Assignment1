Question 1

x = [1,3,4,5,6,7,9] y = [4,7,2,4,7,8,3]

x2 = [2,4,6,8,10] y2 = [5,6,2,6,2]

plt.bar(x,y,label='X-Y compare',color='r') plt.bar(x2,y2,label='X2-Y2 compare',color='b') plt.xlabel("X AXIS") plt.ylabel("Y AXIS") plt.legend()