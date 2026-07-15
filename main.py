# import matplotlib

#pyplot provides a user-friendly interface for plotting
import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)
#
# x=np.array([2023,2024,2025,2026])
# y1=np.array([15,25,30,20])
# y2=np.array([17,23,38,5])
# y3=np.array([13,15,20,30])
# plt.title("Class-size",fontsize=25,
#           family="Arial",
#           fontweight="bold",
#           color="black")
#
# line_style=dict(marker="."
#          ,markersize="30",
#          markerfacecolor="cyan",
#          markeredgecolor="cyan",
#          linestyle="solid",
#          linewidth="4",
#          )#also markersize abbv as ms and 3rd arg abbv as mfc 4th one abbv as mec)
# plt.xlabel("Year",fontsize=10  ,
#            family="Arial",
#            fontweight="bold",
#            color="#223af0")
#
# plt.ylabel("Students",fontsize=10  ,
#            family="Arial",
#            fontweight="bold",
#            color="#223af0")
#
# plt.tick_params(axis="both",
#                 colors="#223af0")
# plt.plot(x,y1,color="#d1f542",**line_style)
# plt.plot(x,y2,color="cyan",**line_style)
# plt.plot(x,y3,color="blue",**line_style)
# plt.xticks(x)
#
#
# #grid()=helps make plots  easier to read by adding reference lines
# plt.grid(axis="y",linewidth=2,
#          color="lightgray",
#          linestyle="dashed")
#
# plt.show()

#plot customization


#making bar chart
categories=["grains","fruit","vegetable","protein","diary","sweets"]
values=np.array([4,3,2,5,3,1])
plt.bar(categories,values,color="skyblue")
# plt.barh(categories,values,color="skyblue")

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()
