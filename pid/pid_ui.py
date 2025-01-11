# 通过将滑动条对象作为参数传递给更新函数update，可以解决无法访问滑动条对象的问题。
# 这样更新函数就能够正确获取滑动条的值，并实现实时更新波形的功能。
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import Scale

import matplotlib
matplotlib.use('Qt5Agg')
# 如果安装PyQt5或PySide2后仍然出现问题，您可以尝试使用其他Matplotlib后端，比如TkAgg 或者 WXAgg。
# 只需将matplotlib.use('Qt5Agg')改为
# matplotlib.use('TkAgg')
#或
#matplotlib.use('WXAgg')


# 初始化参数
Kp = 1.0
Ki = 0.1
Kd = 0.01
setpoint = 10.0

# 创建GUI界面
root = tk.Tk()
root.title('PID Controller')

# 创建滑动条用于调节PID参数
scale_Kp = Scale(root, label='Kp', from_=0, to=2, resolution=0.1, orient='horizontal')
scale_Kp.set(Kp)
scale_Kp.pack()

scale_Ki = Scale(root, label='Ki', from_=0, to=0.2, resolution=0.01, orient='horizontal')
scale_Ki.set(Ki)
scale_Ki.pack()

scale_Kd = Scale(root, label='Kd', from_=0, to=0.02, resolution=0.001, orient='horizontal')
scale_Kd.set(Kd)
scale_Kd.pack()

# 创建画布用于实时显示波形
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlim(0, 20)
ax.set_ylim(-5, 5)

# 更新函数，用于实时更新波形
def update(frame, scale_Kp, scale_Ki, scale_Kd):
    global Kp, Ki, Kd
    Kp = scale_Kp.get()
    Ki = scale_Ki.get()
    Kd = scale_Kd.get()

    output = []
    time = []

    dt = 0.01
    integral = 0.0
    prev_error = 0.0

    for t in np.arange(0, 10, dt):
        error = setpoint - t
        integral += error * dt
        derivative = (error - prev_error) / dt

        control = Kp * error + Ki * integral + Kd * derivative

        output.append(control)
        time.append(t)

        prev_error = error

    line.set_data(time, output)
    return line,

# 创建动画
ani = FuncAnimation(fig, update, fargs=(scale_Kp, scale_Ki, scale_Kd), frames=200, interval=50, blit=False)

# 启动GUI界面
tk.mainloop()
