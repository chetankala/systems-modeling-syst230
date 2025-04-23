import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random

x_vals = list()
y1_vals = []
y2_vals = []

index = count()

def gen_data(i):
    x_vals.append(next(index))
    y1_vals.append(random.randint(-5, 10))
    y2_vals.append(random.randint(-6, 12))
    
    plt.cla()
    
    plt.plot(x_vals, y1_vals, label = "Data 1")
    plt.plot(x_vals, y2_vals, label = "Data 2")
    plt.legend(loc = "upper left")
    
    plt.tight_layout()
    
anim = FuncAnimation(plt.gcf(), gen_data, interval = 1000)

plt.tight_layout()
plt.show()