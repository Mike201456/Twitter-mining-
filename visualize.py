import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("uber.txt","r").read()
    lines = pullData.split('\n')

    xar = []
    yar = []
    val = []
    x = 0
    y = 0
    z = 0

    for l in lines[-200:]:
        x += 1
        if "pos" in l:
            y += 1
            z += 1
        elif "neg" in l:
            y -= 1
        ratio = z/x
        xar.append(x)
        yar.append(y)
        val.append(ratio)
    ax1.clear()
    ax1.plot(xar,val)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
plt.close(fig)


