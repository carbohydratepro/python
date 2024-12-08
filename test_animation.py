import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# 定数を定義する
k = 1
omega = 1
phi_y = 0
phi_z = 0

# xの範囲と刻みを定義する
x = np.arange(0, 4*np.pi, np.pi/10)

# 更新関数
def update(t):
    Ey = np.cos(k*x + phi_y + omega*t)
    Ez = np.cos(k*x + phi_z + omega*t)
    line.set_data(x, Ey)
    line.set_3d_properties(Ez)
    return line,

# 初期の電場の成分を計算する
Ey = np.cos(k*x + phi_y)
Ez = np.cos(k*x + phi_z)

# プロットを作成する
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot(x, Ey, Ez)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("E-field Components")
ax.set_xlabel("X")
ax.set_ylabel("Ey")
ax.set_zlabel("Ez")

# アニメーションを作成する
ani = FuncAnimation(fig, update, frames=range(0, 21), interval=500)

# アニメーションを表示する
plt.show()

