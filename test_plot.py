import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 定数を定義する
t = 0
k = 1
omega = 1
phi_y = 0
phi_z = 0

# xの範囲と刻みを定義する
x = np.arange(0, 4*np.pi, np.pi/10)

# 電場の成分を計算する
Ey = np.cos(k*x + phi_y + omega*t)
Ez = np.cos(k*x + phi_z + omega*t)

# プロットを作成する
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, Ey, Ez)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("E-field Components")
ax.set_xlabel("X")
ax.set_ylabel("Ey")
ax.set_zlabel("Ez")

# グラフを表示する
plt.show()



