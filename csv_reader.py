import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(i):
    file = pd.read_csv('velocidade.csv')
    t = file['tempo']
    v_linear = file['velocidade_linear']
    v_angular = file['velocidade_angular']
    accel_lin = file['acceleração_linear']
    accel_ang = file['acceleração_angular']

    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()

    ax1.plot(v_linear, label = "Velocidade Linear")
    ax2.plot(accel_lin, label = "Acceleração Linear")
    ax3.plot(v_angular, label = "Velocidade Angular")
    ax4.plot(accel_ang, label = "Acceleração Angular")

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper left')
    ax3.legend(loc='upper left')
    ax4.legend(loc='upper left')


    ax2.set_xlabel('Tempo')
    ax4.set_xlabel('Tempo')

plt.style.use('seaborn')

fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
fig2, (ax3, ax4) = plt.subplots(nrows=2, ncols=1)
ani1 = FuncAnimation(fig1, animate, interval=1000)
ani2 = FuncAnimation(fig2, animate, interval=1000)

plt.tight_layout()
plt.show()